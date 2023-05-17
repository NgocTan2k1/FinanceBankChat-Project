from django.urls import path
from api.bank.views import vietstock_finance_statement_view, fireant_finance_statement_view, cafef_finance_statement_view

urlpatterns = [
    path('fireant/',fireant_finance_statement_view.as_view()),
    path('vietstock/',vietstock_finance_statement_view.as_view()),
    path('cafef/', cafef_finance_statement_view.as_view())
]
