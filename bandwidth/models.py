from django.db import models


class Sms(models.Model):
    text = models.TextField(max_length=255)
