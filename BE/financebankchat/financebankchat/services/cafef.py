from django.core.cache import cache as default_cache
import requests
from bs4 import BeautifulSoup

from core.models import debt, income, propertise, provider, stock
"""
Return html data
Please Using Beautifullsoup to seperate or identify
"""
def get_propertise(stock_name, year):
    url = f'https://s.cafef.vn/bao-cao-tai-chinh/{stock_name}/BSheet/{year}/0/0/0/ket-qua-hoat-dong-kinh-doanh-ngan-hang-thuong-mai-co-phan-ngoai-thuong-viet-nam.chn'

    response = requests.get(url)
    if response.status_code != 200:
        return False, ''
    
    soup = BeautifulSoup(response.text, 'html5lib')
    return True, soup


def get_finance_statement(stock_name, year):
    try:
        print(f"start {stock_name}-{year}-cafef")
        url_report = f'https://s.cafef.vn/bao-cao-tai-chinh/{stock_name}/IncSta/{year}/0/0/0/bao-cao-tai-chinh-ngan-hang-thuong-mai-co-phan-ngoai-thuong-viet-nam.chn'
        url_finance = f"https://s.cafef.vn/bao-cao-tai-chinh/{stock_name}/BSheet/{year}/0/0/0/ket-qua-hoat-dong-kinh-doanh-ngan-hang-tmcp-ky-thuong-viet-nam-techcombank.chn"

        response = requests.get(url_report)
        response_finance = requests.get(url_finance)
        if response.status_code != 200 and response_finance.status_code != 200:
            return False, ''

        soup = BeautifulSoup(response.text, 'html5lib')
        soup_finance = BeautifulSoup(response_finance.text, 'html5lib')
        process_data(soup, stock_name)
        process_finance(soup_finance, stock_name)
        return True, "Xử lý xong"
    except Exception as e:
        print(f"error {stock_name}-{year}: {e}")
        return False, ''



def process_data(data: BeautifulSoup, stock_name):
    stock_id = stock.objects.only("id").filter(name=stock_name).first().id
    provider_id = provider.objects.only("id").filter(name="cafef").first().id

    years = data.find_all('td', {'class': "h_t"})
    net_interest_income = data.find('tr', {'id':'20'}).find_all("td",{"class":"b_r_c"})
    profit_after_tax = data.find('tr', {'id':'200'}).find_all("td",{"class":"b_r_c"})
    service_activities = data.find('tr', {'id':'21'}).find_all("td",{"class":"b_r_c"})
    other_activities = data.find('tr', {'id':'61'}).find_all("td",{"class":"b_r_c"})
    interest_income = data.find('tr', {'id':'130'}).find_all("td",{"class":"b_r_c"})
    for index, year in enumerate(years):
        income.objects.update_or_create(
            stock_id=stock_id,
            provider_id=provider_id,
            year=int(year.get_text()),
            defaults={
                'net_interest_income': float(net_interest_income[index + 1].get_text().replace(",", "") or 0)/1000000,
                'profit_after_tax': float(profit_after_tax[index + 1].get_text().replace(",", "") or 0)/1000000,
                'service_activities': float(service_activities[index + 1].get_text().replace(",", "") or 0)/1000000,
                'other_activities': float(other_activities[index + 1].get_text().replace(",", "") or 0)/1000000,
                'interest_income': float(interest_income[index + 1].get_text().replace(",", "") or 0)/1000000,
            }
        )


def process_finance(data: BeautifulSoup, stock_name):
    stock_id = stock.objects.only("id").filter(name=stock_name).first().id
    provider_id = provider.objects.only("id").filter(name="cafef").first().id
    cash = data.find('tr', {'id': '0011'}).find_all("td", {"class": "b_r_c"})
    deposit = data.find('tr', {'id': '00111'}).find_all("td", {"class": "b_r_c"})
    loan_credit_institutions = data.find('tr', {'id': '00112'}).find_all("td", {"class": "b_r_c"})
    loan_customer = data.find('tr', {'id': '0012'}).find_all("td", {"class": "b_r_c"})
    total = data.find('tr', {'id': '001'}).find_all("td", {"class": "b_r_c"})
    total_debt = data.find('tr', {'id': '0020'}).find_all("td", {"class": "b_r_c"})
    years = data.find_all('td', {'class': "h_t"})
    for index, year in enumerate(years):
        propertise.objects.update_or_create(
            stock_id=stock_id,
            provider_id=provider_id,
            year=int(year.get_text()),
            defaults={
                'cash': float(cash[index + 1].get_text().replace(",", "") or 0)/1000000,
                'deposit': float(deposit[index + 1].get_text().replace(",", "") or 0)/1000000,
                'loan_credit_institutions': float(loan_credit_institutions[index + 1].get_text().replace(",", "") or 0)/1000000,
                'loan_customer': float(loan_customer[index + 1].get_text().replace(",", "") or 0)/1000000,
                'total': float(total[index + 1].get_text().replace(",", "") or 0)/1000000,
            }
        )
        debt.objects.update_or_create(
            stock_id=stock_id,
            provider_id=provider_id,
            year=int(year.get_text()),
            defaults={
                'total_debt': float(total_debt[index + 1].get_text().replace(",", "") or 0)/1000000,
            }
        )
