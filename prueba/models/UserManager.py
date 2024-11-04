from django.contrib.auth.models import BaseUserManager
#Archivo agregado
class UsuarioManager(BaseUserManager):
    def create_user(self, clave, password=None, **extra_fields):
        """
        Crea y devuelve un usuario con la clave y contraseña dadas.
        """
        if not clave:
            raise ValueError('El usuario debe tener una clave.')
        
        user = self.model(clave=clave, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, clave, password=None, **extra_fields):
        """
        Crea y devuelve un superusuario con la clave y contraseña dadas.
        """
        extra_fields.setdefault('es_admin', True)

        return self.create_user(clave, password, **extra_fields)
