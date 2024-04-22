from django.shortcuts import render

from rest_framework import viewsets
from .models import PacientesConsulta, PacienteArea
from .serializer import PacientesConsultaSerializer, PacienteAreaSerializer

# from django.http import JsonResponse

class PacienteAreaViewSet(viewsets.ModelViewSet):
	queryset = PacienteArea.objects.all()
	serializer_class = PacienteAreaSerializer
     
class PacientesConsultaViewSet(viewsets.ModelViewSet):
	queryset = PacientesConsulta.objects.all()
	serializer_class = PacientesConsultaSerializer


# def consulta_pacientes(request):
#     pacientes = PacientesConsulta.objects.all()
#     data = [{'id': paciente.id, 'tipo_servicio': paciente.Tipo_servicio} for paciente in pacientes]
#     return JsonResponse(data, safe=False)

# def area_pacientes(request):
#     areas = PacienteArea.objects.all()
#     data = []
#     for area in areas:
#         data.append({
#             'area_medica': area.AreaMedica,
#             'pacientes_en_atencion': area.Pacientes_en_Atencion,
#             'medicos_disponible': area.Medicos_Disponible,
#             'engermeras_disponible': area.Engermeras_Disponible,
#             'pasantes_asignados': area.Pasantes_Asignados,
#             'residentes_asignados': area.Residentes_Asignados
#         })
#     return JsonResponse(data, safe=False)