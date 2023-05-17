from rest_framework import serializers
from core.models import cryption


class CryptionSerializer(serializers.Serializer):
    class Meta:
        model = cryption
        fields = ('pub_key', 'live_time')