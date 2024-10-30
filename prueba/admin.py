from django.contrib import admin

# Register your models here.
from prueba import models


admin.site.register(models.Usuario)
admin.site.register(models.SolicitudJustificante)
admin.site.register(models.RegistroHorario)