from django.contrib.auth.models import AbstractUser
from django.db import models

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
