from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'nacimientos', views.BebeViewSet)
router.register(r'seguimientos', views.SeguimientoPediatricoViewSet)
router.register(r'c_cliente', views.c_clienteViewSet)
router.register(r'c_rol', views.c_rolViewSet)
router.register(r'c_registrosM', views.c_registroViewSet)
router.register(r'solicitud_organos_1', views.solicitud_organos_1ViewSet)
router.register(r'c_dispensacion_medicamentos', views.c_dispensacionViewSet)
router.register(r'c_detalle_dispensacion', views.c_detalle_dispensacionViewSet)
router.register(r'c_detalle_dispensacion_relacion', views.c_detalle_dispensacion_relacionViewSet)
router.register(r'c_lotes_medicamentos', views.c_lotes_medicamentoViewSet)
router.register(r'c_detalle_lotes', views.c_detalle_lotes_medicamentoViewSet)
router.register(r'ServiciosMedicos', views.ServiciosMedicosViewSet)
router.register(r'ServiciosHospitalarios', views.ServiciosHospitalariosViewSet)
router.register(r'AprobacionesServicios', views.AprobacionesServiciosViewSet)
router.register(r'BitacoraDG', views.BitacoraDGServiciosViewSet)
router.register(r'Puesto', views.PuestoViewSet)
router.register(r'Horario', views.HorarioViewSet)
router.register(r'Personal', views.PersonalViewSet)

urlpatterns = [
	path('api/v1',include(router.urls))
]

