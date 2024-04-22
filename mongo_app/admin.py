from django.contrib import admin
from .models import PacientesConsulta, PacienteArea
# Register your models here.
admin.site.register(PacientesConsulta),
admin.site.register(PacienteArea)