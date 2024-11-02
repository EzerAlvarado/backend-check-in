from django.urls import path,include
from rest_framework import routers
from prueba import views


router = routers.DefaultRouter()
router.register('registro-horas', views.RegistroHorarioViewSet)
router.register('solicitudes', views.SolicitudJustificanteViewSet)
router.register('usuarios', views.UsuarioViewSet)

urlpatterns=[
    path('', include(router.urls))
]
