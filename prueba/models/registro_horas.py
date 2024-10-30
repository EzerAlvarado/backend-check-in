from django.db import models

class RegistroHorario(models.Model):
    """
    Modelo de usuarios
    """
    OPCIONES_ESTADO = [
        ('A', 'Aprobada'),
        ('C', 'Cancelada'),
        ('T', 'En Transcurso'),
    ]
    
    clave_empleado = models.IntegerField(null=True,blank=True,help_text='Clave del empleado que registra su horas')

    hora_entrada = models.DateTimeField(null=True,blank=True)

    hora_salida = models.DateTimeField(null=True,blank=True)
    
    llego_tarde = models.BooleanField(default=False,help_text='Si llego 15 min tarde se va a recorrer 1 hora su registro')
    
    se_cancela_su_dia = models.BooleanField(default=False,help_text='llego 2 horas tarde se va va a cancelar el dia')
    
    estado_registro =  models.CharField(
        max_length=1,
        choices=OPCIONES_ESTADO,
    )
    
    usuario_que_registra = models.ForeignKey("prueba.Usuario",
                                             null=True,
                                             blank=True,
                                             related_name='registros_de_horas',
                                             help_text='Relacion al empleaod que hizo el registro, se va a relacionar con la clave que se ortorga ',
                                             on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'registros_de_horas'
        ordering = ['pk']
        verbose_name = 'Registro De Horario'
        verbose_name_plural = 'Registros De Horarios'
        permissions = [
            ['autorizar_registrohora', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_registrohora', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | : {self.nombre} | Clave Usuario: {self.clave}"
