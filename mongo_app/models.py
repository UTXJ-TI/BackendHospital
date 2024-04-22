from django.db import models

# Modelo para la tabla PacientesConsulta
class PacientesConsulta(models.Model):
    # Se define automáticamente como clave primaria
    tipo_servicio = models.CharField(max_length=50)
    numero_recetas = models.CharField(max_length=50)
    numero_estudios_clinicos = models.CharField(max_length=50)
    numero_ingresos = models.CharField(max_length=50)

# Modelo para la tabla PacienteArea
class PacienteArea(models.Model):
    # Se define explícitamente como clave primaria
    area_medica = models.AutoField(primary_key=True)
    pacientes_en_atencion = models.CharField(max_length=50)
    medicos_disponibles = models.CharField(max_length=50)
    enfermeras_disponibles = models.CharField(max_length=50)
    pasantes_asignados = models.CharField(max_length=50)
    residentes_asignados = models.CharField(max_length=50)