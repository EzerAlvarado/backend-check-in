from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from prueba.models import Usuario
from django.contrib.auth.hashers import check_password

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    clave = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Aquí puedes agregar información adicional al token, si es necesario
        return token

    def validate(self, attrs):
        print("Received attributes:", attrs)  # Imprime los atributos recibidos
        clave = attrs.get('clave')
        password = attrs.get('password')

        # Verifica si ambas credenciales están presentes
        if clave is not None and password is not None:
            try:
                user = Usuario.objects.get(clave=clave)
            except Usuario.DoesNotExist:
                print("Usuario no encontrado con la clave proporcionada.")  # Registro adicional
                raise serializers.ValidationError('No active account found with the given credentials.')

            # Verifica la contraseña
            if not user.check_password(password):
                print("Contraseña incorrecta.")  # Registro adicional
                raise serializers.ValidationError('No active account found with the given credentials.')

            attrs['user'] = user
        else:
            print("Faltan credenciales.")  # Registro adicional
            raise serializers.ValidationError('Both "clave" and "password" are required.')

        return attrs
