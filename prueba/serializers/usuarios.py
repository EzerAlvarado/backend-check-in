# Evento serializers.

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
            'clave',       # Usado como nombre de usuario
            'es_admin',
            'contrasenia',
            'password',    # Solo se usa para escribir, no para leer
        )
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}  # Evitar exponer el password en la respuesta

    def create(self, validated_data):
        """Crear un nuevo usuario, encriptando su contraseña."""
        password = validated_data.pop('password', None)
        usuario = Usuario(**validated_data)
        if password:
            usuario.set_password(password)  # Encripta la contraseña
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        """Actualizar un usuario, encriptando la contraseña si se proporciona."""
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)  # Encripta la nueva contraseña

        instance.save()
        return instance
