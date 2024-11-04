"""Evento serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from prueba.models import SolicitudJustificante
from prueba.models import Usuario

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
            'evidencia_pdf',
            'clave_empleado',
            'usuario_que_registra',
        )        
        read_only_fields = ('id',)
        
    def validate_clave_empleado(self, value):
        if not value:
            raise serializers.ValidationError("La clave del empleado es obligatoria.")
        return value

    def create(self, validated_data):
        clave_empleado = validated_data.get('clave_empleado')
        print(clave_empleado)

        # Verificar si el usuario existe
        try:
            usuario = Usuario.objects.get(clave=clave_empleado)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("No existe un usuario con esta clave.")

        # Asignar el usuario que registra
        validated_data['usuario_que_registra'] = usuario

        # Crear y devolver el registro
        return SolicitudJustificante.objects.create(**validated_data)