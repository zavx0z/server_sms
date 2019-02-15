from django.contrib import admin
from bandwidth.models import Sms


class SmsAdmin(admin.ModelAdmin):
    list_display = ('_from', 'to', 'direction', 'time', 'state', 'text')

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Sms, SmsAdmin)
