# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_invitation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='team_leader',
        ),
    ]
