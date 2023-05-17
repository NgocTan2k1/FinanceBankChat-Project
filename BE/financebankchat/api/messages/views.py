
from rest_framework import generics  
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
from core.models import cryption as cryptionModel


from financebankchat.services import message as message_service


class post_message_view(generics.GenericAPIView):
    """
    POST api/v1/message
    """
    allowed_methods = ['POST']
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        message = request.data.get('message')
        user = request.user
        
    
