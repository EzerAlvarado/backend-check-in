"""Evento filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from prueba.models import Evento


class EventoFilter(filters.FilterSet):
    nombre_del_rentador = filters.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = Evento
        fields = (
            'id',
            'nombre_del_rentador',
            'numero_de_celular_rentador',
            'pago_renta',
            'fecha_de_evento',
            'observaciones',
        )        