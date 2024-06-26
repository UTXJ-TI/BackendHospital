from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'nacimientos_bebes', views.nacimientos_bebesViewSet)
router.register(r'seguimiento_pediatria', views.seguimiento_pediatriaViewSet)
router.register(r'c_cliente', views.c_clienteViewSet)
router.register(r'c_rol', views.c_rolViewSet)
router.register(r'c_registrosM', views.c_registroViewSet)
router.register(r'personas', views.personasViewSet)
router.register(r'pacientes', views.pacientesViewSet)
router.register(r'personal_medico', views.personal_medicoViewSet)
router.register(r'organos', views.organosViewSet)
router.register(r'solicitud_transplantes', views.solicitud_transplantesViewSet)
router.register(r'c_dispensacion', views.c_dispensacionViewSet)
#router.register(r'solicitud_organos_1', views.solicitud_organos_1ViewSet)
#router.register(r'c_dispensacion', views.c_dispensacionViewSet)
router.register(r'c_receta_medica', views.c_receta_medicaViewSet)
router.register(r'c_receta_medica_detalles', views.c_receta_medica_detallesViewSet)
#router.register(r'c_inventario', views.c_inventarioViewSet)
router.register(r'ServiciosMedicos', views.ServiciosMedicosViewSet)
router.register(r'ServiciosHospitalarios', views.ServiciosHospitalariosViewSet)
router.register(r'AprobacionesServicios', views.AprobacionesServiciosViewSet)
router.register(r'BitacoraDG', views.BitacoraDGServiciosViewSet)
router.register(r'Departamento', views.DepartamentoServiciosViewSet)
router.register(r'AreaMedicaServicios', views.AreaMedicaServiciosViewSet)
router.register(r'PersonalMedico', views.PersonalMedicoServiciosViewSet)
router.register(r'PersonaServicios', views.PersonaServiciosViewSet)
router.register(r'vista_estado_solicitudes', views.VistaEstadoSolicitudesViewSet)
router.register(r'vista_cantidad_personal_medico', views.VistaCantidadPersonalMedicoViewSet)
router.register(r'vista_pacientes', views.VistaCantidadPacientesViewSet)
router.register(r'vista_operaciones_bitacora', views.VistaOperacionesBitacoraViewSet)
router.register(r'Puesto', views.PuestoViewSet)
router.register(r'Horario', views.HorarioViewSet)
router.register(r'Personal', views.PersonalViewSet)

urlpatterns = [
	path('api/v1',include(router.urls))
]

