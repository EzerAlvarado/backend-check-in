from django.shortcuts import render

# Create your views here.
#models
from prueba.models import SolicitudJustificante
#rest
from rest_framework import viewsets
#utilities
from prueba.serializers.solicitudes import SolicitudJustificanteModelSerializer
#filters
from prueba.filters.solicitudes import SolicitudJustificanteFilter

class SolicitudJustificanteViewSet(viewsets.ModelViewSet):
    """
    View de SolicitudJustificantes
    Maneja CRUD
    """
    queryset=SolicitudJustificante.objects.all()
    serializer_class = SolicitudJustificanteModelSerializer
    filterset_class = SolicitudJustificanteFilter
