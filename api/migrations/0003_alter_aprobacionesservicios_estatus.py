# Generated by Django 5.0.1 on 2024-04-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_vistaestadosolicitudes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprobacionesservicios',
            name='estatus',
            field=models.CharField(choices=[('Aprobado', 'Aprobado'), ('No Aprobado', 'No Aprobado'), ('En Proceso', 'En Proceso'), ('Cancelado', 'Cancelado')], default='En Proceso', max_length=20),
        ),
    ]