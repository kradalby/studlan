# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-08-03 13:17


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0023_auto_20220803_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='frame_background_color',
            field=models.CharField(blank=True, max_length=50, verbose_name='frame background color'),
        ),
        migrations.AddField(
            model_name='tickettype',
            name='frame_foreground_color',
            field=models.CharField(blank=True, max_length=50, verbose_name='frame foreground color'),
        ),
    ]
