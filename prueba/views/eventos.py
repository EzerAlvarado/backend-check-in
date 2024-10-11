from django.shortcuts import render

# Create your views here.
#models
from prueba.models import Evento
#rest
from rest_framework import viewsets
#utilities
from prueba.serializers.eventos import EventoModelSerializer
#filters
from prueba.filters.eventos import EventoFilter

class EventoViewSet(viewsets.ModelViewSet):
    """
    View de Eventos
    Maneja CRUD
    """
    queryset=Evento.objects.all()
    serializer_class = EventoModelSerializer
    filterset_class = EventoFilter
