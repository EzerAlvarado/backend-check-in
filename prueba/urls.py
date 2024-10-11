
from prueba import views
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('eventos', views.EventoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
]
