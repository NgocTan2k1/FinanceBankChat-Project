from rest_framework import serializers

from core.models import cryption, provider, stock


class provider_serializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = provider


class stock_serializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = stock

class cryption_serializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("pri_key",)
        model = stock
