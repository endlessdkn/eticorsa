# Generated by Django 4.1.3 on 2022-11-29 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0006_envios_reciboclisse_envios_recibolaser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envios',
            name='FechaPreparacion',
            field=models.CharField(choices=[(47, datetime.date(2022, 11, 21)), (48, datetime.date(2022, 11, 29)), (49, datetime.date(2022, 12, 7))], help_text='La fecha puede ser este dia, 7 dias antes o 7 dias despues', max_length=250, verbose_name='Semana de Produccion'),
        ),
    ]
