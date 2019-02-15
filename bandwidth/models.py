from django.db import models


class Sms(models.Model):
    text = models.TextField('текст сообщения', max_length=255, blank=True, null=True)
    eventType = models.TextField('тип события', max_length=50, blank=True, null=True)
    direction = models.TextField('направление', max_length=5, blank=True, null=True)
    _from = models.TextField('от', max_length=12, blank=True, null=True)
    to = models.TextField('в', max_length=12, blank=True, null=True)
    time = models.DateTimeField('время', blank=True, null=True)
    state = models.TextField('состояние', max_length=20, blank=True, null=True)

