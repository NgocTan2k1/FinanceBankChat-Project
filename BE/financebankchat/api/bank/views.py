
from rest_framework import  generics, permissions
from rest_framework.response import Response

from financebankchat.services import fireant, vietstock, cafef

class fireant_finance_statement_view(generics.GenericAPIView):
    """
    GET api/v1/bank/fireant/
    """
    resource_name = 'finance_statement'
    allowed_methods = ['GET']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        name=self.request.GET.get('name')
        data = fireant.get_finance_statement(name)
        return Response({"result": data})
    
class vietstock_finance_statement_view(generics.GenericAPIView):
    """
    api/v1/bank/vietstock/
    """
    resource_name = 'finance_statement'
    allowed_methods = ['GET']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        name=self.request.GET.get('name')
        year=self.request.GET.get('year')
        data = vietstock.get_finance_statement(name,year)
        
        return Response({"result": data})
    

class cafef_finance_statement_view(generics.GenericAPIView):
    """
    api/v1/bank/cafef/
    """
    resource_name = 'finance_statement'
    allowed_methods = ['GET']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        name=self.request.GET.get('name')
        year=self.request.GET.get('year')
        data = cafef.get_finance_statement(name,year)
        
        return Response({"result": data})

