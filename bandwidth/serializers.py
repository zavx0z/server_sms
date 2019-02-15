from rest_framework import serializers
from bandwidth.models import Sms


class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sms
        fields = '__all__'
