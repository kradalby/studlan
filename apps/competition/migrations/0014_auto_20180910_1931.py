# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-10 19:31


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0013_competition_tournament_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='max_participants',
            field=models.SmallIntegerField(default=0, help_text=b'The maximum number of participants allowed for a competition.Restricts participants based on competition type. 0 means infinite participants are allowed.', verbose_name=b'Maximum participants'),
        ),
    ]
