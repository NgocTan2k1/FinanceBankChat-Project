import requests
import re
from django.core.cache import cache as default_cache

from core.models import debt, income, propertise, provider, stock
from django.db import transaction

def get_finance_statement(stock_name: str):
    try:
        print(f"start {stock_name}-fireant")
        success, token = _get_token()
        if not success:
            return {"messages": "Lấy token thấy bại"}
        url_report = f'https://restv2.fireant.vn/symbols/{stock_name}/full-financial-reports?type=2&year=2023&quarter=0&limit=13'
        url_report_propertise = f"https://restv2.fireant.vn/symbols/{stock_name}/full-financial-reports?type=1&year=2023&quarter=0&limit=13"
        headers = {
            'authorization': f"Bearer {token}"
        }

        report_propertise = requests.get(url_report_propertise, headers=headers)
        report = requests.get(url_report, headers=headers)
        if report.status_code == 200 and report_propertise.status_code ==200:
            process_data(report.json(), stock_name)
            process_propertise(report_propertise.json(), stock_name)
            return report.json()
    except Exception as e:
        print(f"error: {stock_name} : {e}")
    return ""


def process_data(data, stock_name):
    stock_id = stock.objects.only("id").filter(name=stock_name).first().id
    provider_id = provider.objects.only("id").filter(name="fireant").first().id
    with transaction.atomic():
        for index, period in enumerate(data[0].get("values")):
            year = period.get("year")
            income.objects.update_or_create(
                stock_id=stock_id,
                provider_id=provider_id,
                year=year,
                defaults={
                    'net_interest_income': float(data[0].get("values")[index].get("value") or 0)/1000000,
                    'profit_after_tax': float(data[20].get("values")[index].get("value") or 0)/1000000,
                    'service_activities': float(data[3].get("values")[index].get("value") or 0)/1000000,
                    'other_activities': float(data[9].get("values")[index].get("value") or 0)/1000000,
                    'interest_income': float(data[16].get("values")[index].get("value") or 0)/1000000,
                }
            )

def process_propertise(data, stock_name):
    stock_id = stock.objects.only("id").filter(name=stock_name).first().id
    provider_id = provider.objects.only("id").filter(name="fireant").first().id
    with transaction.atomic():
        for index, period in enumerate(data[0].get("values")):
            year = period.get("year")
            propertise.objects.update_or_create(
                stock_id=stock_id,
                provider_id=provider_id,
                year=year,
                defaults={
                    'cash': float(data[1].get("values")[index].get("value") or 0)/1000000,
                    'deposit': float(data[2].get("values")[index].get("value") or 0)/1000000,
                    'loan_credit_institutions': float(data[6].get("values")[index].get("value") or 0)/1000000,
                    'loan_customer': float(data[12].get("values")[index].get("value") or 0)/1000000,
                    'total': float(data[46].get("values")[index].get("value") or 0)/1000000,
                }
            )
            debt.objects.update_or_create(
                stock_id=stock_id,
                provider_id=provider_id,
                year=year,
                defaults={
                    'total_debt': float(data[75].get("values")[index].get("value") or 0)/1000000,
                }
            )

    

    



def _get_token():
    if token:= default_cache.get('fireant_token'):
        return True, token
    url = 'https://fireant.vn/static/js/main.56c5180e.chunk.js'
    response = requests.get(url)
    if response.status_code != 200:
        return False, ''
    token = re.findall("getState\(\),o=\"(.*?)\";", response.text)
    if len(token) == 1:
        default_cache.set('fireant_token', token[0], 60*60)
        return True, token[0]
    return False,''