
from datetime import datetime
import pytz
from rest_framework import generics, permissions
from rest_framework.response import Response

from api.configs.serializers import cryption_serializer, provider_serializer
from api.pagination import MediumResultsSetPagination
from core.models import provider, stock, cryption
from financebankchat.services.cryption import get_token
from financebankchat.settings import RECAPTCHA_PUBLIC_KEY

class provider_views(generics.ListAPIView):
    """
    POST api/v1/configs/provider/
    """
    resource_name = 'finance_statement'
    allowed_methods = ['GET']
    serializer_class = provider_serializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return provider.objects.all()


class stock_views(generics.ListAPIView):
    """
    POST api/v1/configs/stock
    """
    resource_name = 'finance_statement'
    allowed_methods = ['GET']
    serializer_class = provider_serializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = MediumResultsSetPagination


    def get_queryset(self):
        return stock.objects.all()
    

class config_views(generics.GenericAPIView):
    """
    POST api/v1/configs/login
    """
    resource_name = 'finance_statement'
    allowed_methods = ['GET']
    serializer_class = cryption_serializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = MediumResultsSetPagination

    def get(self, request, *args, **kwargs):
        if res := cryption.objects.filter(user=None, live_time__gt=datetime.now()).first():
            return Response({"public_key": res.pub_key, "expire": res.live_time}, status=200)

        pub, pri, exp = get_token(30)
        cryption.objects.update_or_create(
            user=None, 
            defaults={'live_time': exp, 'pub_key': pub, 'pri_key': pri})
        return Response({"public_key" : pub , "expire" : exp}, status=200)
    
    """
    import React from 'react';
    import ReCAPTCHA from 'react-google-recaptcha';

    const MyComponent = () => {
    const handleRecaptcha = (token) => {
        "g-captcha-response": token
        console.log(token);
    }

    return (
        <div>
        <ReCAPTCHA
            sitekey="YOUR_SITE_KEY"
            onChange={handleRecaptcha}
        />
        </div>
    );
    };

    export default MyComponent;
    """

