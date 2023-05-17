import base64
from datetime import datetime
from django.shortcuts import render
import pytz
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
from rest_framework import exceptions, generics, permissions
from rest_framework.response import Response
from app.serializers import EmptySerializer

from app.throttle import CaptchaThrottle
from core.models import cryption
from financebankchat.helper.data_helper import process_data
from financebankchat.services.cryption import decrypt_message
from financebankchat.settings import ENVIRONMENT

class login_gcaptcha(TokenObtainPairView):
    """Normal login endpoint.

    POST token/

    Raises:
        exceptions.Throttled: 3req/hr
    """

    permission_classes = [permissions.AllowAny]
    throttle_classes = (CaptchaThrottle,)

    def post(self, request, *args, **kwargs):
        key_pair = cryption.objects.filter(user=None).first()
        now = datetime.now()
        if now > key_pair.live_time:
            return Response(status=400, data={"messages":"cryption live fail"})
        crawl_pass = decrypt_message(base64.b64decode(request.data['password']), key_pair.pri_key)
        crawl_username = decrypt_message(base64.b64decode(request.data['username']), key_pair.pri_key)
        request.data['password'] = crawl_pass
        request.data['username'] = crawl_username
        return super().post(request, *args, **kwargs)

    def throttled(self, request, wait):
        if ENVIRONMENT in ['production']:
            raise exceptions.Throttled(detail={
                "message": "Invalid captcha",
            })
        

class processdata(generics.GenericAPIView):
    """
    process data
    POST run_data/
    """
    permission_classes = [permissions.AllowAny]
    resource_name = 'processdata'
    serializer_class = EmptySerializer
    allowed_methods = ['POST']

    def get(self, requests, *args, **kwargs):
        return Response(status=200, data={"messages": "sucesss"})

    def post(self, requests, *args, **kwargs):
        process_data()
        return Response(status =200, data={"messages":"sucesss"})
