"""Evento filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from prueba.models import Usuario


class UsuarioFilter(filters.FilterSet):

    class Meta:
        model = Usuario
        fields = (
            'id',
            'nombre',
            'clave',
            'es_admin',
        )        