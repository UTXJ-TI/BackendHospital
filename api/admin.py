from django.contrib import admin
from .models import c_cliente,c_rol,c_registrosM, c_cirugia,c_Solicitud_Cirugias, nacimientosBebes,SeguimientoPediatrico,ServiciosMedicos, ServiciosHospitalarios, AprobacionesServicios,BitacoraDG, Puesto, Horario, Personal, c_dispensacion_medicamentos,c_detalle_dispensacion, c_detalle_dispensacion_relacion,c_lotes_medicamentos,c_detalle_lotes

# Register your models here.
admin.site.register(nacimientosBebes)
admin.site.register(SeguimientoPediatrico)
admin.site.register(c_cliente)
admin.site.register(c_rol)
admin.site.register(c_registrosM)
admin.site.register(c_cirugia)
admin.site.register(c_Solicitud_Cirugias)
admin.site.register(c_dispensacion_medicamentos)
admin.site.register(c_detalle_dispensacion)
admin.site.register(c_detalle_dispensacion_relacion)
admin.site.register(c_lotes_medicamentos)
admin.site.register(c_detalle_lotes)
admin.site.register(ServiciosMedicos)
admin.site.register(ServiciosHospitalarios)
admin.site.register(AprobacionesServicios)
admin.site.register(BitacoraDG)
admin.site.register(Puesto)
admin.site.register(Horario)
admin.site.register(Personal)
