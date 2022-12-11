# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-09 04:39


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0019_auto_20200619_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='lan',
            name='frontpage_media_link',
            field=models.CharField(blank=True, help_text='URL for embedded media on front page.', max_length=300, verbose_name='frontpage media link'),
        ),
        migrations.AddField(
            model_name='lan',
            name='frontpage_media_type',
            field=models.CharField(choices=[(b'image', 'Image'), (b'video', 'Video'), (b'stream', 'Stream')], default=b'image', help_text='Type of the optional embedded media on front page.', max_length=10, verbose_name='frontpage media type'),
        ),
    ]
