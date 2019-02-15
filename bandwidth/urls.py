from rest_framework import routers
from .api import SmsViewSet

router = routers.DefaultRouter()

router.register('bandwidth', SmsViewSet, 'sms')
urlpatterns = router.urls
