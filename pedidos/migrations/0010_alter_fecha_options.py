# Generated by Django 4.0 on 2021-12-30 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0009_servicio_calif'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fecha',
            options={'ordering': ['-fecha'], 'verbose_name': 'fecha', 'verbose_name_plural': 'fechas'},
        ),
    ]
