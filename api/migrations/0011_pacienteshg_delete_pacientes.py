# Generated by Django 4.1.13 on 2024-04-17 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_pacientes_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacientesHG',
            fields=[
                ('persona', models.OneToOneField(db_column='Persona_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.persona')),
                ('nss', models.CharField(blank=True, db_column='NSS', max_length=15, null=True, unique=True)),
                ('tipo_seguro', models.CharField(db_column='Tipo_Seguro', max_length=50)),
                ('fecha_registro', models.DateTimeField(db_column='Fecha_Registro')),
                ('fecha_ultimacita', models.DateTimeField(db_column='Fecha_UltimaCita')),
                ('estatus_medico', models.CharField(blank=True, db_column='Estatus_Medico', max_length=100, null=True)),
                ('estatus_vida', models.CharField(db_column='Estatus_Vida', max_length=10)),
                ('estatus', models.TextField(blank=True, db_column='Estatus', null=True)),
            ],
            options={
                'db_table': 'api_pacientes',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Pacientes',
        ),
    ]