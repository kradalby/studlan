# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seating', '0003_seating_ticket_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seating',
            name='ticket_type',
            field=models.ForeignKey(blank=True, to='lan.TicketType', help_text=b'Leaving this field blank will leave the seating open to any tickets for the given LAN', null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
