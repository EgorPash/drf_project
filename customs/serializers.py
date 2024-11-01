from rest_framework import serializers
from customs.models import Customs
from customs.validators import CustomsValidator


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customs
        fields = '__all__'
        validators = [CustomsValidator]