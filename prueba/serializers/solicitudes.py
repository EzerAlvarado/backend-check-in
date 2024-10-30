"""Evento serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from prueba.models import SolicitudJustificante

class SolicitudJustificanteModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un SolicitudJustificante
    """

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
        read_only_fields = ('id',)