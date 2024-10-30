"""Evento serializers."""

# Django
from django.db.models import Q
from django.contrib.auth.hashers import make_password

# Django REST Framework
from rest_framework import serializers

# Models
from prueba.models import Usuario

class UsuarioModelSerializer(serializers.ModelSerializer):
    """
    Serializer para crear, editar, obtener y eliminar
    a un Usuario.
    """

    class Meta:
        model = Usuario
        fields = (
            'id',
            'nombre',
            'clave',
            'es_admin',
            'password',  
        )
        read_only_fields = ('id',) 
        
    def create(self, validated_data):
        """Crear un nuevo usuario, encriptando su contraseña."""
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])  # Usar el método para establecer la contraseña
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        """Actualizar un usuario, encriptando la contraseña si se proporciona."""
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)  # Usar el método para establecer la nueva contraseña

        instance.save()
        return instance