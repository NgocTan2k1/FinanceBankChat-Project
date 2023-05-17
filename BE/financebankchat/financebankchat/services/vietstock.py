from bs4 import BeautifulSoup
import requests

from django.core.cache import cache

from core.models import debt, income, propertise, provider, stock
"""
{
    "data": [
        {
            "ReportNormId": 4385,
            "ReportNormName": "Thu nhập lãi thuần",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4386,
            "ReportNormName": "Lãi/lỗ thuần từ hoạt động dịch vụ",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4387,
            "ReportNormName": "Lãi/lỗ thuần từ hoạt động kinh doanh ngoại hối và vàng",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4388,
            "ReportNormName": "Lãi/lỗ thuần từ mua bán chứng khoán kinh doanh",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4389,
            "ReportNormName": "Lãi/lỗ thuần từ mua bán chứng khoán đầu tư",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4390,
            "ReportNormName": "Lãi/lỗ thuần từ hoạt động khác",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4393,
            "ReportNormName": "Thu nhập từ góp vốn, mua cổ phần",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4391,
            "ReportNormName": "Chi phí hoạt động",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4376,
            "ReportNormName": "Lợi nhuận thuần từ hoạt động kinh doanh trước chi phí dự phòng rủi ro tín dụng",
            "CssStyle": "NormalB",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4392,
            "ReportNormName": "Chi phí dự phòng rủi ro tín dụng",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4377,
            "ReportNormName": "Tổng lợi nhuận trước thuế",
            "CssStyle": "NormalB",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4378,
            "ReportNormName": "Lợi nhuận sau thuế",
            "CssStyle": "NormalB",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4380,
            "ReportNormName": "Lợi nhuận sau thuế của cổ đông của Ngân hàng mẹ",
            "CssStyle": "NormalB",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4381,
            "ReportNormName": "Lãi cơ bản trên cổ phiếu (VNÐ)",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Kết quả kinh doanh",
            "ReportTypeCode": "KQ"
        },
        {
            "ReportNormId": 4302,
            "ReportNormName": "Tài sản",
            "CssStyle": "NormalB",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4310,
            "ReportNormName": "Tiền mặt, vàng bạc, đá quý",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4311,
            "ReportNormName": "Tiền gửi tại NHNN",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4312,
            "ReportNormName": "Tiền, vàng gửi tại các TCTD khác và cho vay các TCTD khác",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4313,
            "ReportNormName": "Chứng khoán kinh doanh",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4314,
            "ReportNormName": "Các công cụ tài chính phái sinh và các tài sản tài chính khác",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4315,
            "ReportNormName": "Cho vay và cho thuê tài chính khách hàng",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4316,
            "ReportNormName": "Chứng khoán đầu tư",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4317,
            "ReportNormName": "Góp vốn, đầu tư dài hạn",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4307,
            "ReportNormName": "Tài sản cố định",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4308,
            "ReportNormName": "Bất động sản đầu tư",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4327,
            "ReportNormName": "Tài sản Có khác",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4375,
            "ReportNormName": "Tổng cộng tài sản",
            "CssStyle": "NormalB",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4303,
            "ReportNormName": "Nợ phải trả và vốn chủ sở hữu",
            "CssStyle": "NormalB",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4318,
            "ReportNormName": "Các khoản nợ Chính phủ và NHNN",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4319,
            "ReportNormName": "Tiền gửi và vay các TCTD khác",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4320,
            "ReportNormName": "Tiền gửi của khách hàng",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4321,
            "ReportNormName": "Các công cụ tài chính phái sinh và các khoản nợ tài chính khác",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4322,
            "ReportNormName": "Vốn tài trợ, ủy thác đầu tư, cho vay mà TCTD chịu rủi ro",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4323,
            "ReportNormName": "Phát hành giấy tờ có giá",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4324,
            "ReportNormName": "Các khoản nợ khác",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4325,
            "ReportNormName": "Vốn và các quỹ",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4306,
            "ReportNormName": "Lợi ích của cổ đông thiểu số",
            "CssStyle": "Normal",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 4305,
            "ReportNormName": "Tổng nợ phải trả và vốn chủ sở hữu",
            "CssStyle": "NormalB",
            "Unit": "",
            "ReportTypeName": "Cân đối kế toán",
            "ReportTypeCode": "CD"
        },
        {
            "ReportNormId": 53,
            "ReportNormName": "Thu nhập trên mỗi cổ phần của 4 quý gần nhất (EPS)",
            "CssStyle": "",
            "Unit": "VNĐ",
            "ReportTypeName": "Chỉ số tài chính",
            "ReportTypeCode": "CSTC"
        },
        {
            "ReportNormId": 54,
            "ReportNormName": "Giá trị sổ sách của cổ phiếu (BVPS)",
            "CssStyle": "",
            "Unit": "VNĐ",
            "ReportTypeName": "Chỉ số tài chính",
            "ReportTypeCode": "CSTC"
        },
        {
            "ReportNormId": 55,
            "ReportNormName": "Chỉ số giá thị trường trên thu nhập (P/E)",
            "CssStyle": "",
            "Unit": "Lần",
            "ReportTypeName": "Chỉ số tài chính",
            "ReportTypeCode": "CSTC"
        },
        {
            "ReportNormId": 57,
            "ReportNormName": "Chỉ số giá thị trường trên giá trị sổ sách (P/B)",
            "CssStyle": "",
            "Unit": "Lần",
            "ReportTypeName": "Chỉ số tài chính",
            "ReportTypeCode": "CSTC"
        },
        {
            "ReportNormId": 45,
            "ReportNormName": "Tỷ suất lợi nhuận trên vốn chủ sở hữu bình quân (ROEA)",
            "CssStyle": "",
            "Unit": "%",
            "ReportTypeName": "Chỉ số tài chính",
            "ReportTypeCode": "CSTC"
        },
        {
            "ReportNormId": 47,
            "ReportNormName": "Tỷ suất sinh lợi trên tổng tài sản bình quân (ROAA)",
            "CssStyle": "",
            "Unit": "%",
            "ReportTypeName": "Chỉ số tài chính",
            "ReportTypeCode": "CSTC"
        }
    ]
}
"""
def get_verify_code(stock_name):
    url=f'https://finance.vietstock.vn/{stock_name}/tai-chinh.htm?tab=BCTT'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }
    session = requests.session()
    response = session.get(url, headers=headers)
    if response.status_code != 200:
        return False, '', ''
    soup = BeautifulSoup(response.text, 'html5lib')
    cookie = ';'.join([f'{name}={value}' for (name, value) in session.cookies.get_dict().items()])
    
    csrf_token = soup.find('form', {'action': f"/{stock_name}/tai-chinh.htm"}).find("input").attrs.get('value')
    return True, cookie, csrf_token


def get_finance_statement(stock_name, year):
    try:
        print(f"start {stock_name}-{year}-vietstock")
        if results:= cache.get(f'vietstock_results_{year}_{stock_name}'):
            return True, results
        
        success, cookie, verify_code = get_verify_code(stock_name)  
        if not success:
            return False, ''
        
        # report_data = cache.get(f'vietstock_report_{year}_{stock_name}')
        success, data = get_report_id(cookie, verify_code, stock_name)
        total_count = len(data.get('data'))
        if not success:
            return False, ''
        for dt in data.get('data'):
            cache.set(f"vietstock_report_{dt.get('YearPeriod')}_{stock_name}", dt)
            if int(year) == dt.get('YearPeriod'):
                report_data = dt
        success, results = get_stock(
            cookie=cookie, 
            verify_code=verify_code, 
            stock_name=stock_name,
            year=year, 
            report_data=report_data,
            total_count=total_count
        )
        process_data(results.get("data"), stock_name, year)
        cache.set(f'vietstock_results_{year}_{stock_name}', results)
        return True, results
    except Exception as e:
        print(f"error {stock_name}-{year}: {e}")
        return False, ''


def get_report_id(cookie, verify_code, stock_name,):
    url = "https://finance.vietstock.vn/data/BCTT_GetListReportData"
    payload = {
        "StockCode": stock_name,
        "UnitedId": -1,
        "Unit":1000000,
        "IsNamDuongLich": "false",
        "PeriodType": "NAM",
        "SortTimeType":"Time_ASC",
        "__RequestVerificationToken":verify_code
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    response = requests.post(url, headers=headers, data=payload)
    return (False, '') if response.status_code != 200 else (True, response.json())
    


def get_stock(cookie, verify_code, stock_name, *args, **kwargs):
    url = "https://finance.vietstock.vn/data/GetReportDataDetailValue_BCTT_ByReportDataIds"
    payload = {
        "StockCode": stock_name,
        "Unit": "1000000",
        "listReportDataIds[0][Index]":0,
        "listReportDataIds[0][ReportDataId]": kwargs.get('report_data').get("ReportDataID"),
        "listReportDataIds[0][IsShowData]": kwargs.get('report_data').get("IsShowData_Permission"),
        "listReportDataIds[0][RowNumber]": kwargs.get('report_data').get("RowNumber"),
        "listReportDataIds[0][YearPeriod]":kwargs.get('report_data').get('YearPeriod'),
        "listReportDataIds[0][TotalCount]": kwargs.get("total_count"),
        "listReportDataIds[0][SortTimeType]":"Time_ASC",
        "__RequestVerificationToken": verify_code
    }


    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie" : cookie,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }

    response = requests.post(url=url, headers=headers, data=payload)
    if response.status_code == 200:
        return True, response.json()
    return False, response.text


def process_data(data, stock_name, year):
    stock_id = stock.objects.only("id").filter(name=stock_name).first().id
    provider_id = provider.objects.only("id").filter(name="vietstock").first().id
    income.objects.update_or_create(
        stock_id=stock_id,
        provider_id=provider_id,
        year=year,
        defaults={
            'net_interest_income': float(data[29].get("Value1") or 0),
            'profit_after_tax': float(data[25].get("Value1") or 0),
            'service_activities': float(data[30].get("Value1") or 0),
            'other_activities': float(data[34].get("Value1") or 0),
            'interest_income': float(data[26].get("Value1") or 0),
        }
    )
    propertise.objects.update_or_create(
        stock_id=stock_id,
        provider_id=provider_id,
        year=year,
        defaults={
            'cash': float(data[6].get("Value1") or 0),
            'deposit': float(data[7].get("Value1") or 0),
            'loan_credit_institutions': float(data[8].get("Value1") or 0),
            'loan_customer': float(data[11].get("Value1") or 0),
            'total': float(data[23].get("Value1") or 0),
        }
    )
    debt.objects.update_or_create(
        stock_id=stock_id,
        provider_id=provider_id,
        year=year,
        defaults={
            'total_debt':  float(data[2].get("Value1")or 0),
        }
    )
