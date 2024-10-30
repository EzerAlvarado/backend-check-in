"""Evento filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from prueba.models import RegistroHorario


class RegistroHorarioFilter(filters.FilterSet):

    class Meta:
        model = RegistroHorario
        fields = (
            'id',
            'hora_entrada',
            'hora_salida',
            'llego_tarde',
            'se_cancela_su_dia',
            'estado_registro',
            'usuario_que_registra',
        )        