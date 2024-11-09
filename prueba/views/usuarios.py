from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from prueba.models import Usuario
from prueba.serializers.usuarios import UsuarioModelSerializer
from prueba.filters.usuarios import UsuarioFilter

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    View de Usuarios
    Maneja CRUD
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioModelSerializer
    filterset_class = UsuarioFilter

    def destroy(self, request, *args, **kwargs):
        # Obtener el ID del usuario autenticado
        current_user_id = request.user.id
        # Obtener el ID del usuario que se intenta eliminar
        target_user_id = kwargs['pk']

        # Verificar si el usuario intenta eliminarse a sí mismo
        if str(current_user_id) == target_user_id:
            return Response(
                {"detail": "No puedes eliminar tu propio usuario."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Si no es el mismo usuario, proceder con la eliminación
        return super().destroy(request, *args, **kwargs)
