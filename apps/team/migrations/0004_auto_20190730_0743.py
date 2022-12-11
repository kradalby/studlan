# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-30 07:43


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_remove_invitation_team_leader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invitee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
