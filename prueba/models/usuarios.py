from django.db import models
from django.contrib.auth.hashers import make_password, check_password
class Usuario(models.Model):
    """
    Modelo de usuarios
    """
    nombre = models.CharField(max_length=150,null=True,blank=True,help_text='Nombre del usuario')

    clave = models.IntegerField(null=True, blank=True, unique=True, help_text='Clave que se usara de Acceso')
    
    es_admin = models.BooleanField(default=False,help_text='Booleano que indica si el usuario es admin')

    password = models.CharField(max_length=128,null=True,blank=True,help_text='Contraseña encriptada del usuario administrador')
    
    class Meta:
        db_table = 'usuarios'
        ordering = ['pk']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        permissions = [
            ['autorizar_usuario', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_usuario', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2'):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """Verifica la contraseña proporcionada."""
        return check_password(raw_password, self.password)

    def set_password(self, raw_password):
        """Establece la contraseña encriptada."""
        self.password = make_password(raw_password)
        
    def __str__(self):
        return f"Pk: {self.pk} | Nombre Del Usuario: {self.nombre} | Clave Usuario: {self.clave}"