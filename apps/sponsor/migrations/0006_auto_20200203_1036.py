# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-03 10:36


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0005_auto_20190729_0513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'verbose_name': 'partner', 'verbose_name_plural': 'partners'},
        ),
        migrations.AlterModelOptions(
            name='sponsorrelation',
            options={'ordering': ['-priority'], 'verbose_name': 'partner relation', 'verbose_name_plural': 'partner relations'},
        ),
        migrations.AlterModelOptions(
            name='sponsortranslation',
            options={'verbose_name': 'partner translation', 'verbose_name_plural': 'partner translations'},
        ),
        migrations.AlterField(
            model_name='sponsorrelation',
            name='priority',
            field=models.IntegerField(help_text='Higher priority means closer to the top of the partner list.', verbose_name='priority'),
        ),
        migrations.AlterField(
            model_name='sponsorrelation',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sponsor.Sponsor', verbose_name='partner'),
        ),
        migrations.AlterField(
            model_name='sponsortranslation',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='sponsor.Sponsor', verbose_name=b'Partner'),
        ),
    ]
