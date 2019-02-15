from bandwidth.models import Sms
from rest_framework import viewsets, permissions
from .serializers import SmsSerializer


class SmsViewSet(viewsets.ModelViewSet):
    queryset = Sms.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SmsSerializer
