from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from prueba.serializers.TokenObtainPairSerializer import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'nombre': user.nombre,
                'clave': user.clave,
                'es_admin': user.es_admin,
            }
        })
