from django.db import models


class Sms(models.Model):
    text = models.TextField('текст сообщения', max_length=255)
    eventType = models.TextField('тип события', max_length=50)
    direction = models.TextField('направление', max_length=5)
    _from = models.TextField('от', max_length=12)
    to = models.TextField('в', max_length=12)
    time = models.DateTimeField('время')
    state = models.TextField('состояние', max_length=20)

