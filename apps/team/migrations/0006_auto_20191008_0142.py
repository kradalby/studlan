# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-10-08 01:42


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_auto_20190730_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['tag', 'title'], 'permissions': (('show_invitations', 'Show users invited to teams'),), 'verbose_name': 'team', 'verbose_name_plural': 'teams'},
        ),
    ]
