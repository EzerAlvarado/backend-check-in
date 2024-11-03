"""Evento filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from prueba.models import Usuario


class UsuarioFilter(filters.FilterSet):
    clave = filters.NumberFilter(lookup_expr='exact')
    class Meta:
        model = Usuario
        fields = (
            'id',
            'nombre',
            'clave',
            'contrasenia',
            'es_admin',
        )