"""Evento filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from prueba.models import SolicitudJustificante


class SolicitudJustificanteFilter(filters.FilterSet):

    class Meta:
        model = SolicitudJustificante
        fields = (
            'id',
            'estado_solicitud',
            'motivo',
            'dia_justificar',
            'clave_empleado',
            'usuario_que_registra',
        )        