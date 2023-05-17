from datetime import datetime
import openai
import os
from core.models import stock

from financebankchat.helper.sql_helper import query_to_dict
from financebankchat.services.dp import noise_rows
from financebankchat.settings import OPENAI_API_KEY, OPENAI_MAX_TOKEN

openai.api_key = OPENAI_API_KEY
prov = {
    "1": "fireant",
    "2": "vietstock",
    "3": "cafef",
}
table = [
    "core_provider(id: str, name: str, alias)",
    "core_stock(id: str, name: str, alias)",
    "core_propertise(id: str, stock_id: str, provider_id: str, year, cash, deposit, loan_credit_institutions,loan_customer, total)",
    "core_debt(id: str, stock_id: str, provider_id: str, year, bad_debt, total_debt)",
    "core_income(id: str, stock_id: str, provider_id: str, year, net_interest_income, interest_income, service_activities,other_activities, profit_after_tax)",
    # "core_index(id: str, stock_id: str, provider_id: str, year, NPL, LEV)",
    # "core_stock_index(id: str, stock_id: str, provider_id: str, ROE, ROA, EPS, PA,)",
]


def get_template_sql(question, provider_id = None, stock_id=None, year=None, **kwargs):
    try:
        year = list(range(year[0],year[1])) if year else []
        provider_id = str(provider_id).replace("[", "").replace("]", "") if provider_id or provider_id != [] else ''
        stock_id = str(stock_id).replace("[", "").replace("]", "") if stock_id or stock_id != []  else ''
        year = str(year).replace("[", "").replace("]", "") if year or year != []  else ''

        stock_template = f"stock_id là '{stock_id}'" if stock_id else "limit 3"
        provider_template = f"provider_id là '{provider_id}'" if provider_id else ""
        if year and year != ['']:
            provider_template += f"với year = '{year}' sắp xếp năm từ bé đến lớn"

        template = "### Postgres SQL tables, with their properties: \n" + "#\n"
        for i in table:
            template += f"# {i}" + "\n"

        template += "#\n"
        query_conditions = f"{provider_template} và {stock_template}"
        template += (
            f"""###Let't query this question: \"{question} và {query_conditions}\" \n"""
        )

        stop = ['#' , ';']
        return template , stop
    except Exception as e:
        return '', ''



def get_template_is_bank_industry(question):
    template = f"ngân hàng:{question}"
    stop = ['#' , ';']
    return template , stop


def getTemplate(type_ques, data, **kwargs):
    if type_ques == "sql":
        return get_template_sql(data, **kwargs)
    elif type_ques == "text":
        return get_template_is_bank_industry(data)
    else:
        return f"{data['question']} {data['answer']}" , None

def chat_gpt(message , stop) :
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        temperature=0.9,
        max_tokens=OPENAI_MAX_TOKEN,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=stop,
    )
    return response.choices[0].text


def convert_table(data: dict, stock_list: list) -> dict:
    # sourcery skip: low-code-quality
    if isinstance(data, str):
        return {
            "element": [],
            "types": "text",
            "message": data
        }
    types = "vertical" if len(stock_list) <= 2 else "line"
    years, providers, elements, stocks = set(), set(), set(), set()
    message = "đây là thông tin: "

    for dt in data:
        if dt.get("year"): years.add(int(dt.get("year")))
        if dt.get("provider_id"): providers.add(dt.get("provider_id"))
        if dt.get("stock_id"): stocks.add(dt.get("stock_id"))
        for key, value in dt.items():
            elements.add(key)

    stock_name = {stk.id: stk.name for stk in stock.objects.filter(id__in=stocks)}

    tables = {}
    years = sorted(years)
    elements.difference_update({"provider_id", "year", "stock_id", "id"})
    for element in elements:
        if not tables.get(element):
            tables[element] = {
                "title": element,
            }
            for provider_id in providers:
                tables[element][prov[provider_id]] = {
                    stock_name[stock_id]: {"dataRaw": [], "years": []}
                    for stock_id in stocks
                }
        for dt in data:
            pro_name = prov[dt["provider_id"]]
            sto_name = stock_name[dt["stock_id"]]
            cyear = tables[element][pro_name][sto_name]["years"][-1] + 1 if tables[element][pro_name][sto_name]["years"] else next(iter(years))
            while cyear != int(dt.get("year")) and cyear < datetime.now().year:
                tables[element][pro_name][sto_name]["dataRaw"].append(0)
                tables[element][pro_name][sto_name]["years"].append(cyear)
                cyear+=1
            
            if cyear == datetime.now().year:
                continue

            tables[element][pro_name][sto_name]["dataRaw"].append(dt.get(element))
            tables[element][pro_name][sto_name]["years"].append(dt.get("year"))
        tables[element]["years"] = list(years)
        message += f"\n -{element}"
    return {
        "table": tables,
        "elements": list(elements),
        "types": types,
        "message": message
    }

def process_question(question: str, **kwargs):
    template, stop = getTemplate('sql', question, **kwargs)
    results = ''
    if template:
        query = chat_gpt(template, stop)
        success, data = query_to_dict(query)
        if success:
            results = noise_rows(data)
    
    if not template or not success:
        template, stop = getTemplate('text', question)
        results = chat_gpt(template, stop)

    data = convert_table(results, kwargs.get("stock_id"))
    return data

## example
# {
#     "result": {
#         "table": {
#             "bad_debt": {
#                 "title": "bảng bad_debt",
#                 "fireant": {
#                     "ACB": {
#                         "dataRaw": [
#                             2.5766591659487705,
#                             0.0
#                         ],
#                         "years": [
#                             2017,
#                             2018
#                         ]
#                     },
#                     "ABB": {
#                         "dataRaw": [
#                             0.0,
#                             2.7433996259862417
#                         ],
#                         "years": [
#                             2017,
#                             2018
#                         ]
#                     }
#                 },
#                 "years": [
#                     2017,
#                     2018
#                 ]
#             },
#             "total_debt": {
#                 "title": "bảng total_debt",
#                 "fireant": {
#                     "ACB": {
#                         "dataRaw": [
#                             284316120.3839724,
#                             329333241.0
#                         ],
#                         "years": [
#                             2017,
#                             2018
#                         ]
#                     },
#                     "ABB": {
#                         "dataRaw": [
#                             84503069.0,
#                             89997894.80845888
#                         ],
#                         "years": [
#                             2017,
#                             2018
#                         ]
#                     }
#                 },
#                 "years": [
#                     2017,
#                     2018
#                 ]
#             }
#         },
#         "elements": [
#             "bad_debt",
#             "total_debt"
#         ],
#         "types": "vertical",
#         "message": "đây là thông tin: \n -bad_debt\n -total_debt"
#     }
# }
