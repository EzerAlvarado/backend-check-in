"""Evento filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from prueba.models import RegistroHorario


class RegistroHorarioFilter(filters.FilterSet):
    clave_empleado = filters.NumberFilter(lookup_expr='exact')
    class Meta:
        model = RegistroHorario
        fields = (
            'id',
            'hora_entrada',
            'clave_empleado',
            'hora_salida',
            'llego_tarde',
            'se_cancela_su_dia',
            'estado_registro',
            'total_horas',
            'usuario_que_registra',
        )        