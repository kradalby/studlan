# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0010_match_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='challonge_url',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Challonge url', blank=True),
            preserve_default=True,
        ),
    ]
