from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from financebankchat.services import cryption as cryptionService
from api.cryption.serializer import CryptionSerializer
from core.models import cryption as cryptionModel
class get_token_view(generics.GenericAPIView): 
    """
    POST api/v1/cryption
    """
    allowed_methods = ['POST']
    serializer_class = CryptionSerializer
    permission_classes = [IsAuthenticated,]
    def post(self, request , *args, **kwargs):
        user = request.user
        pub , pri , exp = cryptionService.get_token()
        cryptionModel.objects.update_or_create(user=user , defaults={'live_time': exp , 'pub_key': pub , 'pri_key': pri})
        return Response({"public_key" : pub , "expire" : exp}, status=200)
