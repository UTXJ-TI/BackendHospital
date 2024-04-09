from django.contrib import admin
from .models import c_cliente,c_rol,c_registrosM, c_cirugia,c_Solicitud_Cirugias, nacimientos_bebes,seguimiento_pediatria, c_dispensacion,c_receta_medica,c_receta_medica_detalles,c_inventario,ServiciosMedicos, ServiciosHospitalarios, AprobacionesServicios,BitacoraDG, Puesto, DepartamentoPuesto, HorarioPersonal, Personal

# Register your models here.
admin.site.register(nacimientos_bebes)
admin.site.register(seguimiento_pediatria)
admin.site.register(c_cliente)
admin.site.register(c_rol)
admin.site.register(c_registrosM)
admin.site.register(c_cirugia)
admin.site.register(c_Solicitud_Cirugias)
admin.site.register(c_dispensacion)
admin.site.register(c_receta_medica)
admin.site.register(c_receta_medica_detalles)
admin.site.register(c_inventario)
admin.site.register(ServiciosMedicos)
admin.site.register(ServiciosHospitalarios)
admin.site.register(AprobacionesServicios)
admin.site.register(BitacoraDG)
admin.site.register(Puesto)
admin.site.register(DepartamentoPuesto)
admin.site.register(HorarioPersonal)
admin.site.register(Personal)
