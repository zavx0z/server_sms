from rest_framework import serializers
from bandwidth.models import Sms


class SmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sms
        fields = ['text', 'eventType', 'direction', 'from', 'to', 'time', 'state']
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


SmsSerializer._declared_fields["from"] = serializers.CharField(source="_from")
