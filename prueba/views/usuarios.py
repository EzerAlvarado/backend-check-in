from django.shortcuts import render

# Create your views here.
#models
from prueba.models import Usuario
#rest
from rest_framework import viewsets
#utilities
from prueba.serializers.usuarios import UsuarioModelSerializer
#filters
from prueba.filters.usuarios import UsuarioFilter
from rest_framework.permissions import AllowAny

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    View de Usuarios
    Maneja CRUD
    """
    queryset=Usuario.objects.all()
    serializer_class = UsuarioModelSerializer
    filterset_class = UsuarioFilter
