from rest_framework import serializers
from .models import c_cliente,c_rol, c_registrosM, solicitud_organos_1,nacimientosBebes, SeguimientoPediatrico, ServiciosMedicos,ServiciosHospitalarios,AprobacionesServicios,BitacoraDG, Puesto, Horario, Personal, c_dispensacion_medicamentos,c_detalle_dispensacion,c_detalle_dispensacion_relacion, c_lotes_medicamentos,c_detalle_lotes

# Serializador para ver/obtener información de un bebé
class BebeSerializer(serializers.ModelSerializer):
    class Meta:
        model = nacimientosBebes
        fields = '__all__'

# Serializador para crear/actualizar información de un bebé
class BebeCrearSerializer(serializers.ModelSerializer):
    class Meta:
        model = nacimientosBebes
        exclude = ['id']  # Excluimos el campo 'id' ya que es autoincremental

# Serializador para ver/obtener información de seguimiento pediátrico
class SeguimientoPediatricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguimientoPediatrico
        fields = '__all__'

# Serializador para crear/actualizar información de seguimiento pediátrico
class SeguimientoPediatricoCrearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguimientoPediatrico
        exclude = ['id_paciente'] 
  
  
class c_clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = c_cliente
        fields = '__all__'
        
class c_rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = c_rol
        fields = '__all__'
  
# FARMACIA
class c_dispensacionSerializer(serializers.ModelSerializer):  
    class Meta:
        model = c_dispensacion_medicamentos
        fields = '__all__'
class c_detalle_dispensacionSerializer(serializers.ModelSerializer):  
    class Meta:
        model = c_detalle_dispensacion
        fields = '__all__'
  
class c_detalle_dispensacion_relacionSerializer(serializers.ModelSerializer):  
    class Meta:
        model = c_detalle_dispensacion_relacion
        fields = '__all__'

class c_lotesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = c_lotes_medicamentos
        fields = '__all__'
        
class c_detalle_lotesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = c_detalle_lotes
        fields = '__all__'



class Meta:
		model = c_rol
		fields = '__all__'
  
class c_registroSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_registrosM
		fields = '__all__'
  
class solicitud_organos_1Serializer(serializers.ModelSerializer):
	class Meta:
		model = solicitud_organos_1
		fields = '__all__'

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
