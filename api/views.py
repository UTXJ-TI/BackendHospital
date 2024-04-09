from rest_framework import viewsets
from .models import c_cliente,c_rol,c_registrosM, nacimientos_bebes,seguimiento_pediatria,personas, pacientes, personal_medico, organos, solicitud_transplantes, Puesto, Horario, Personal, c_cliente,c_rol,c_dispensacion_medicamentos,c_receta_medica,c_receta_medica_detalles,ServiciosMedicos,ServiciosHospitalarios,AprobacionesServicios,BitacoraDG
from .serializer import c_clienteSerializer,c_rolSerializer,c_registroSerializer, nacimientos_bebesSerializer,seguimiento_pediatriaSerializer,personasSerializer, pacientesSerializer, personal_medicoSerializer, organosSerializer, solicitud_transplantesSerializer,c_inventarioSerializer,c_clienteSerializer,c_dispensacionSerializer,c_receta_medicaSerializer,c_receta_medica_detallesSerializer, ServiciosMedicosSerializer, ServiciosHospitalariosSerializer, AprobacionesServiciosSerializer,BitacoraDGServiciosSerializer, PuestoSerializer, HorarioSerializer, PersonalSerializer

class nacimientos_bebesViewSet(viewsets.ModelViewSet):
	queryset = nacimientos_bebes.objects.all()
	serializer_class = nacimientos_bebesSerializer
	
class seguimiento_pediatriaViewSet(viewsets.ModelViewSet):
	queryset = seguimiento_pediatria.objects.all()
	serializer_class = seguimiento_pediatriaSerializer

class c_clienteViewSet(viewsets.ModelViewSet):
	queryset = c_cliente.objects.all()
	serializer_class = c_clienteSerializer

class c_rolViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_rolSerializer
 
class c_registroViewSet(viewsets.ModelViewSet):
	queryset = c_registrosM.objects.all()
	serializer_class = c_registroSerializer
	
class personasViewSet(viewsets.ModelViewSet):
	queryset = personas.objects.all()
	serializer_class = personasSerializer
	
class pacientesViewSet(viewsets.ModelViewSet):
	queryset = pacientes.objects.all()
	serializer_class = pacientesSerializer
	
class personal_medicoViewSet(viewsets.ModelViewSet):
	queryset = personal_medico.objects.all()
	serializer_class = personal_medicoSerializer
	
class organosViewSet(viewsets.ModelViewSet):
	queryset = organos.objects.all()
	serializer_class = organosSerializer
	
class solicitud_transplantesViewSet(viewsets.ModelViewSet):
	queryset = solicitud_transplantes.objects.all()
	serializer_class = solicitud_transplantesSerializer


class c_dispensacionViewSet(viewsets.ModelViewSet):
	queryset = c_dispensacion_medicamentos.objects.all()
	serializer_class = c_dispensacionSerializer

class c_receta_medicaViewSet(viewsets.ModelViewSet):
	queryset = c_receta_medica.objects.all()
	serializer_class = c_receta_medicaSerializer

class c_receta_medica_detallesViewSet(viewsets.ModelViewSet):
	queryset = c_receta_medica_detalles.objects.all()
	serializer_class = c_receta_medica_detallesSerializer

class ServiciosMedicosViewSet(viewsets.ModelViewSet):
	queryset = ServiciosMedicos.objects.all()
	serializer_class = ServiciosMedicosSerializer

class ServiciosHospitalariosViewSet(viewsets.ModelViewSet):
	queryset = ServiciosHospitalarios.objects.all()
	serializer_class = ServiciosHospitalariosSerializer

class AprobacionesServiciosViewSet(viewsets.ModelViewSet):
	queryset = AprobacionesServicios.objects.all()
	serializer_class = AprobacionesServiciosSerializer

class BitacoraDGServiciosViewSet(viewsets.ModelViewSet):
	queryset = BitacoraDG.objects.all()
	serializer_class = BitacoraDGServiciosSerializer

class PuestoViewSet(viewsets.ModelViewSet):
	queryset = Puesto.objects.all()
	serializer_class = PuestoSerializer

class HorarioViewSet(viewsets.ModelViewSet):
	queryset = Horario.objects.all()
	serializer_class = HorarioSerializer

class PersonalViewSet(viewsets.ModelViewSet):
	queryset = Personal.objects.all()
	serializer_class = PersonalSerializer





