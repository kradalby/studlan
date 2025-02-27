# -*- coding: utf-8 -*-


from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(related_name='profile', to=settings.AUTH_USER_MODEL, unique=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
