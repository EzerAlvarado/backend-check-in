from django.shortcuts import render

# Create your views here.
#models
from prueba.models import RegistroHorario
#rest
from rest_framework import viewsets
#utilities
from prueba.serializers.registro_horas import RegistroHorarioModelSerializer
#filters
from prueba.filters.registro_horas import RegistroHorarioFilter
from rest_framework.permissions import AllowAny

class RegistroHorarioViewSet(viewsets.ModelViewSet):
    """
    View de RegistroHorarios
    Maneja CRUD
    """
    queryset=RegistroHorario.objects.all()
    serializer_class = RegistroHorarioModelSerializer
    filterset_class = RegistroHorarioFilter
    permission_classes = (AllowAny,)
