from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager  #Agregado

# CLASE AGREGADA Agregado
class UsuarioManager(BaseUserManager):
    def create_user(self, clave, password=None, **extra_fields):
        if not clave:
            raise ValueError('El usuario debe tener una clave.')
        
        user = self.model(clave=clave, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, clave, password=None, **extra_fields):
        extra_fields.setdefault('es_admin', True)
        return self.create_user(clave, password, **extra_fields)


class Usuario(AbstractUser):
    """
    Modelo de usuario personalizado que extiende AbstractUser.
    """
    clave = models.IntegerField(null=True, blank=True, unique=True, help_text='Clave de acceso única')
    es_admin = models.BooleanField(default=False, help_text='Indica si el usuario tiene privilegios de administrador')
    nombre = models.CharField(max_length=150, null=True, blank=True, help_text='Nombre completo del usuario')
    contrasenia = models.CharField(max_length=200,null=True,blank=True,help_text='Contraseña de usuario pa la movida esa')
    username = None
    
    USERNAME_FIELD = 'clave'  
    REQUIRED_FIELDS = [] 

    objects = UsuarioManager() # Asigna el manager personalizado
    class Meta:
        db_table = 'usuarios'
        ordering = ['pk']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        permissions = [
            ['autorizar_usuario', f'Puede autorizar {verbose_name_plural}'],
            ['viewcrud_usuario', f'Puede visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Nombre: {self.nombre} | Clave Usuario: {self.clave}"
