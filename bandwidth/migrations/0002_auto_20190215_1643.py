# Generated by Django 2.1.7 on 2019-02-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandwidth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sms',
            name='_from',
            field=models.TextField(blank=True, max_length=12, null=True, verbose_name='от'),
        ),
        migrations.AddField(
            model_name='sms',
            name='direction',
            field=models.TextField(blank=True, max_length=5, null=True, verbose_name='направление'),
        ),
        migrations.AddField(
            model_name='sms',
            name='eventType',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='тип события'),
        ),
        migrations.AddField(
            model_name='sms',
            name='state',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='состояние'),
        ),
        migrations.AddField(
            model_name='sms',
            name='time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время'),
        ),
        migrations.AddField(
            model_name='sms',
            name='to',
            field=models.TextField(blank=True, max_length=12, null=True, verbose_name='в'),
        ),
        migrations.AlterField(
            model_name='sms',
            name='text',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='текст сообщения'),
        ),
    ]
