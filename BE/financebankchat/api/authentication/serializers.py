from rest_framework import serializers
from django.contrib.auth.models import User

class register_serializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
