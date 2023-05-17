
import base64
from datetime import datetime
import pytz
from rest_framework import  generics, permissions
from rest_framework.response import Response
from api.authentication.serializers import register_serializer
from core.models import cryption
from financebankchat.security.authentication import register_user
from financebankchat.services.cryption import decrypt_message


class register_user_view(generics.GenericAPIView):
    """
    POST api/v1/authentication/register/
    """
    resource_name = 'register user'
    allowed_methods = ['GET','POST']
    serializer_class = register_serializer
    permission_classes=[permissions.AllowAny,]

    def post(self, request, *args, **kwargs):
        key_pair = cryption.objects.filter(user=None).first()
        now = datetime.now()
        if now > key_pair.live_time:
            return Response(status=400, data={"messages":"cryption live fail"})
        
        username = decrypt_message(base64.b64decode(request.data.get('username')), key_pair.pri_key)
        pass1 = decrypt_message(base64.b64decode(request.data.get('password1')), key_pair.pri_key)
        pass2 = decrypt_message(base64.b64decode(request.data.get('password2')), key_pair.pri_key)
        email = decrypt_message(base64.b64decode(request.data.get('email')), key_pair.pri_key)
        success, msg = register_user(
            username=username,
            password1=pass1,
            password2=pass2,
            email=email
        )
        
        return Response(
            status=200 if success else 400, 
            data={
            'message': msg,
        })
        
