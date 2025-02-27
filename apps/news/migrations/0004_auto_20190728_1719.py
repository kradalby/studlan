# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-28 17:19


import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_pinned'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': 'news article', 'verbose_name_plural': 'news articles'},
        ),
        migrations.AlterModelOptions(
            name='articletranslation',
            options={'verbose_name': 'news article translation', 'verbose_name_plural': 'news article translations'},
        ),
        migrations.AlterField(
            model_name='article',
            name='pinned',
            field=models.BooleanField(default=False, help_text='Pinned articles are shown before non-pinned ones.', verbose_name='pinned'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='article',
            name='relevant_to',
            field=models.ManyToManyField(blank=True, to='lan.LAN', verbose_name='relevant LANs'),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='translated_body',
            field=models.TextField(verbose_name='content'),
        ),
    ]
