# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-24 14:11


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0013_auto_20190814_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='marketing_optin',
            field=models.BooleanField(default=False, help_text='Accept marketing emails about future LANs and stuff.', verbose_name='marketing opt-in'),
        ),
    ]
