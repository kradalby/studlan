# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-25 23:01


import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0009_auto_20170916_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime.now, help_text=b'When the tickets will be made available', verbose_name=b'release date'),
        ),
        migrations.AddField(
            model_name='tickettype',
            name='priority',
            field=models.IntegerField(default=0, help_text=b'In what priority the tickets will show, higher number will show first.', verbose_name=b'Prioity'),
        ),
    ]
