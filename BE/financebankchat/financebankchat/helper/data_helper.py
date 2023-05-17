from threading import Thread

from core.models import stock
from financebankchat.services.fireant import get_finance_statement as fi
from financebankchat.services.vietstock import get_finance_statement as vi
from financebankchat.services.cafef import get_finance_statement as ca


def process_data():
    stock_list = stock.objects.all().values_list("name", flat=True)
    year_list = list(range(2010, 2023))
    _process_fireant(stock_list)
    _process_vietstock(stock_list, year_list)
    _process_cafef(stock_list, year_list)

def _process_fireant(stock_list):
    process_len = 0
    tasks = []
    for name in stock_list:
        task = Thread(target=fi, args=(name,))
        task.start()
        process_len+=1
        if process_len >= 200:
            [task.join() for task in tasks]
            tasks = []
            process_len = 0
        tasks.append(task)

    [task.join() for task in tasks]


def _process_cafef(stock_list, years):
    process_len = 0
    tasks = []
    for name in stock_list:
        for year in years:
            task = Thread(target=ca, args=(name, year))
            task.start()
            process_len += 1
            if process_len >= 200:
                [task.join() for task in tasks]
                tasks = []
                process_len = 0
            tasks.append(task)
    [task.join() for task in tasks]


def _process_vietstock(stock_list, years):
    tasks = []
    process_len = 0
    for name in stock_list:
        for year in years:
            task = Thread(target=vi, args=(name, year))
            task.start()
            process_len += 1
            if process_len >= 300:
                [task.join() for task in tasks]
                tasks = []
                process_len = 0
            tasks.append(task)

    [task.join() for task in tasks]

        

