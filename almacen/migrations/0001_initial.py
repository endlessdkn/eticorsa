# Generated by Django 4.1.3 on 2022-11-26 03:13

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barniz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreBarniz', models.CharField(max_length=50, verbose_name='Nombre del Barniz')),
                ('TipoCobertura', models.CharField(choices=[('Registro', 'A Registro'), ('Base', 'Base')], max_length=50, verbose_name='Tipo de Cobertura')),
                ('DescripcionBarniz', models.TextField(blank=True, null=True, verbose_name='Descripcion del Barniz')),
            ],
            options={
                'verbose_name': 'Barniz',
                'verbose_name_plural': 'Barnices',
                'db_table': 'Barniz',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Clisse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreClisse', models.CharField(max_length=75, verbose_name='Nombre del Clisse')),
                ('ImgClisse', models.ImageField(upload_to='static/desing/clisse', verbose_name='Imagen del Clisse')),
            ],
            options={
                'verbose_name': 'Clisse',
                'verbose_name_plural': 'Clisses',
                'db_table': 'Clisse',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Foil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreFoil', models.CharField(max_length=75, verbose_name='Codigo del Foil')),
                ('ColorFoil', models.CharField(max_length=75, verbose_name='Color del Foil')),
                ('AcabadoFoil', models.CharField(blank=True, max_length=275, null=True, verbose_name='Acabado del Foil')),
                ('PresentacionFoil', models.CharField(max_length=250, verbose_name='Presentacion del Foil')),
            ],
            options={
                'verbose_name': 'Foil',
                'verbose_name_plural': 'Foils',
                'db_table': 'Foil',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Laminado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreLaminado', models.CharField(max_length=75, verbose_name='Nombre del Laminado')),
                ('AcabadoLaminado', models.CharField(max_length=125, verbose_name='Tipo de Laminado')),
                ('DescripcionLaminado', models.CharField(blank=True, max_length=275, null=True, verbose_name='Descriptcion del Laminado')),
                ('AnchoLaminado', models.CharField(max_length=275, verbose_name='Ancho del Laminado')),
                ('PresentacionLaminado', models.CharField(max_length=275, verbose_name='Presentacion del Laminado')),
            ],
            options={
                'verbose_name': 'Laminado',
                'verbose_name_plural': 'Laminados',
                'db_table': 'Laminado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Laser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreLaser', models.CharField(max_length=75, verbose_name='Nombre del Acabado Laser')),
                ('TipoLaser', models.CharField(choices=[('Corte', 'Corte'), ('Grabado', 'Grabado')], max_length=15, verbose_name='Tipo de Acabado')),
                ('ImgLaser', models.ImageField(upload_to='static/desing/laser', verbose_name='Imagen del Clisse')),
            ],
            options={
                'verbose_name': 'laser',
                'verbose_name_plural': 'laser',
                'db_table': 'Laser',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Papel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombrePapel', models.CharField(max_length=50, verbose_name='Nombre del Papel')),
                ('Presentacion', models.CharField(max_length=50, verbose_name='Presentacion del Papel')),
                ('PzasPresentacion', models.SmallIntegerField(blank=True, null=True, verbose_name='Piezas por presentacion')),
                ('Gramaje', models.CharField(max_length=250, verbose_name='Gramaje del Papel')),
            ],
            options={
                'verbose_name': 'Papel',
                'verbose_name_plural': 'Papeles',
                'db_table': 'Papel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Suaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumSuaje', models.CharField(max_length=5, verbose_name='Numero del Suaje')),
                ('TipoSuaje', models.CharField(choices=[('C', 'Colgante'), ('A', 'Adherible'), ('T', 'Tallera'), ('V', 'Vampiro'), ('B', 'Botonera'), ('G', 'Corte Guillotina')], max_length=5, verbose_name='Tipo de Suaje')),
                ('NomSuaje', models.CharField(max_length=50, verbose_name='Nombre del Suaje')),
                ('MedidaEtiqueta', models.CharField(max_length=50, verbose_name='Medida de la Etiqueta')),
                ('MedidaPapel', models.CharField(max_length=50, verbose_name='Medida del Papel')),
                ('CantEtiqueta', models.SmallIntegerField(verbose_name='Piezas en Suaje')),
            ],
            options={
                'verbose_name': 'Suaje',
                'verbose_name_plural': 'Suajes',
                'db_table': 'Suaje',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tinta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreTinta', models.CharField(max_length=250, verbose_name='Nombre Color')),
                ('Color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None)),
                ('Pantone', models.CharField(max_length=50, verbose_name='Codigo Pantone')),
                ('Formula', models.CharField(blank=True, max_length=250, null=True, verbose_name='Formula del Color')),
            ],
            options={
                'verbose_name': 'Tinta',
                'verbose_name_plural': 'Tintas',
                'db_table': 'Tinta',
                'managed': True,
            },
        ),
    ]
