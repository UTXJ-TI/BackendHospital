from rest_framework import serializers
from .models import c_cliente,c_rol, c_registrosM,nacimientos_bebes,seguimiento_pediatria, c_receta_medica, c_receta_medica_detalles, ServiciosMedicos,ServiciosHospitalarios,AprobacionesServicios,BitacoraDG,Departamentos,AreaMedica,PersonalMedico,Personas,Pacientes, VistaEstadoSolicitudes,VistaCantidadPersonalMedico, VistaCantidadPacientes, VistaOperacionesBitacora, Puesto, Horario, Personal 

class nacimientos_bebesSerializer(serializers.ModelSerializer):
	class Meta:
		model = nacimientos_bebes
		fields = '__all__'
		
class seguimiento_pediatriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = seguimiento_pediatria
		fields = '__all__'
class c_clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = c_cliente
        fields = '__all__'
        
class c_rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = c_rol
        fields = '__all__'
  
#Modelo de farmacia  

# class c_dispensacionSerializer(serializers.ModelSerializer):  # Renombrado a c_dispensacionSerializer
#     class Meta:
#         model = c_dispensacion_medicamentos
#         fields = '__all__'
# class c_detalles_dispensacionSerializer(serializers.ModelSerializer):  # Renombrado a c_dispensacionSerializer
#     class Meta:
#         model = c_detalles_dispensacion
#         fields = '__all__'
  
# class c_lotesSerializer(serializers.ModelSerializer):  # Renombrado a c_inventarioSerializer
#     class Meta:
#         model = c_lotes_medicamentos
#         fields = '__all__'
        
# class c_detalles_lotesSerializer(serializers.ModelSerializer):  # Renombrado a c_inventarioSerializer
#     class Meta:
#         model = c_detalle_lotes
#         fields = '__all__'
  
class c_receta_medicaSerializer(serializers.ModelSerializer):  # Renombrado a c_receta_medicaSerializer
    class Meta:
        model = c_receta_medica
        fields = '__all__'
  
class c_receta_medica_detallesSerializer(serializers.ModelSerializer):  # Renombrado a c_receta_medica_detallesSerializer
    class Meta:
        model = c_receta_medica_detalles
        fields = '__all__'


class Meta:
		model = c_rol
		fields = '__all__'
  
class c_registroSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_registrosM
		fields = '__all__'
  
#class solicitud_organos_1Serializer(serializers.ModelSerializer):
#	class Meta:
#		model = solicitud_organos_1
#		fields = '__all__'

class ServiciosMedicosSerializer(serializers.ModelSerializer):
	class Meta:
		model = ServiciosMedicos
		fields = '__all__'

class ServiciosHospitalariosSerializer(serializers.ModelSerializer):
	class Meta:
		model = ServiciosHospitalarios
		fields = '__all__'

class AprobacionesServiciosSerializer(serializers.ModelSerializer):
	class Meta:
		model = AprobacionesServicios
		fields = '__all__'

class BitacoraDGServiciosSerializer(serializers.ModelSerializer):
	class Meta:
		model = BitacoraDG
		fields = '__all__'

class DepartamentoServiciosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Departamentos
		fields = '__all__'

class AreaMedicaServiciosSerializer(serializers.ModelSerializer):
	class Meta:
		model = AreaMedica
		fields = '__all__'

class PersonalMedicoServiciosSerializer(serializers.ModelSerializer):
	class Meta:
		model = PersonalMedico
		fields = '__all__'

class PacientesHGServiciosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pacientes
		fields = '__all__'


class PersonaServiciosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Personas
		fields = '__all__'

class VistaEstadoSolicitudesSerializer (serializers.ModelSerializer):
	class Meta:
		model = VistaEstadoSolicitudes
		fields = '__all__'

class VistaCantidadPersonalMedicoSerializer (serializers.ModelSerializer):
	class Meta:
		model = VistaCantidadPersonalMedico
		fields = '__all__'

class VistaCantidadPacientesSerializer (serializers.ModelSerializer):
	class Meta:
		model = VistaCantidadPacientes
		fields = '__all__'

class VistaOperacionesBitacoraSerializer (serializers.ModelSerializer):
	class Meta:
		model = VistaOperacionesBitacora
		fields = '__all__'


# class ColeccionSerializer (serializers.ModelSerializer):
# 	class Meta:
# 		model = Coleccion
# 		fields = '__all__'




class PuestoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Puesto
		fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Horario
		fields = '__all__'


class PersonalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Personal
		fields = '__all__'
