from django.contrib import admin
from django.urls import path, include  # Importar include para agregar URLs de otras aplicaciones
from rest_framework.routers import DefaultRouter
from prueba.views import CustomTokenObtainPairView 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from prueba import views

# Configuración del router
router = DefaultRouter()
router.register('registro-horas', views.RegistroHorarioViewSet)
router.register('solicitudes', views.SolicitudJustificanteViewSet)
router.register('usuarios', views.UsuarioViewSet)

# Configuración de las URLs
urlpatterns = [
    path("admin/", admin.site.urls),  # URL para el panel de administración
    path("api/", include(router.urls)),  # Incluye las rutas del router bajo el prefijo 'api/'
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
