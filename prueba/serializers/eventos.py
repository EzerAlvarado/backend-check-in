"""Evento serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from prueba.models import Evento

class EventoModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Evento
    """

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
        read_only_fields = ('id',)