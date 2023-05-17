from rest_framework import serializers


class question_serializer(serializers.Serializer):
   question = serializers.CharField()
   provider_id = serializers.ListField()
   stock_id = serializers.ListField()
   year = serializers.ListField()

