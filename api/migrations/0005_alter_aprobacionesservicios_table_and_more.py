# Generated by Django 4.1.13 on 2024-04-22 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_areamedica_departamentos_personas_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='aprobacionesservicios',
            table='aprobaciones_servicios',
        ),
        migrations.AlterModelTable(
            name='bitacoradg',
            table='bitacora_dg',
        ),
        migrations.AlterModelTable(
            name='servicioshospitalarios',
            table='servicios_hospitalarios',
        ),
        migrations.AlterModelTable(
            name='serviciosmedicos',
            table='instalaciones',
        ),
    ]
