from rest_framework import serializers
from .models import PacientesConsulta, PacienteArea


class PacientesConsultaSerializer(serializers.ModelSerializer):
	class Meta:
		model = PacientesConsulta
		fields = '__all__'

class PacienteAreaSerializer(serializers.ModelSerializer):
	class Meta:
		model = PacienteArea
		fields = '__all__'
          

