# Generated by Django 4.1.3 on 2022-11-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_merge_20221129_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opedido',
            name='Indicaciones',
            field=models.TextField(blank=True, help_text='Aqui van algunas opservaciones especiales dentro del pedido', null=True, verbose_name='Indicaciones'),
        ),
    ]
