"""Evento serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from prueba.models import RegistroHorario
from prueba.models import Usuario

class RegistroHorarioModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un RegistroHorario
    """

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
            'usuario_que_registra',
        )   
        read_only_fields = ('id',)
        
    def validate_clave_empleado(self, value):
        if not value:
            raise serializers.ValidationError("La clave del empleado es obligatoria.")
        return value
        
    def validate_hora_entrada(self, value):
        """Verifica que se haya registrado la hora de entrada si la clave es válida."""
        clave_empleado = self.initial_data.get('clave_empleado')  # Obtener el valor de clave_empleado del input

        if clave_empleado and not value:
            raise serializers.ValidationError("La hora de entrada es obligatoria si la clave del empleado es válida.")

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
        return RegistroHorario.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """Actualiza un registro horario existente."""
        instance.clave_empleado = validated_data.get('clave_empleado', instance.clave_empleado)
        instance.hora_entrada = validated_data.get('hora_entrada', instance.hora_entrada)
        instance.hora_salida = validated_data.get('hora_salida', instance.hora_salida)
        instance.llego_tarde = validated_data.get('llego_tarde', instance.llego_tarde)
        instance.se_cancela_su_dia = validated_data.get('se_cancela_su_dia', instance.se_cancela_su_dia)
        instance.estado_registro = validated_data.get('estado_registro', instance.estado_registro)
        instance.usuario_que_registra = validated_data.get('usuario_que_registra', instance.usuario_que_registra)
        instance.save()
        return instance