# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-25 12:11


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0002_auto_20150107_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='logo',
        ),
    ]
