from django.contrib import admin
from .models import c_cliente,c_rol,c_registrosM, c_cirugia,c_Solicitud_Cirugias, nacimientos_bebes,seguimiento_pediatria, c_dispensacion_medicamentos,c_detalles_dispensacion, c_lotes_medicamentos,c_detalle_lotes,c_receta_medica,c_receta_medica_detalles,ServiciosMedicos, ServiciosHospitalarios, AprobacionesServicios,BitacoraDG, Puesto, Horario, Personal

# Register your models here.
admin.site.register(nacimientos_bebes)
admin.site.register(seguimiento_pediatria)
admin.site.register(c_cliente)
admin.site.register(c_rol)
admin.site.register(c_registrosM)
admin.site.register(c_cirugia)
admin.site.register(c_Solicitud_Cirugias)
admin.site.register(c_dispensacion_medicamentos)
admin.site.register(c_receta_medica)
admin.site.register(c_receta_medica_detalles)
admin.site.register(c_detalles_dispensacion)
admin.site.register(c_lotes_medicamentos)
admin.site.register(c_detalle_lotes)
admin.site.register(ServiciosMedicos)
admin.site.register(ServiciosHospitalarios)
admin.site.register(AprobacionesServicios)
admin.site.register(BitacoraDG)
admin.site.register(Puesto)
admin.site.register(Horario)
admin.site.register(Personal)
