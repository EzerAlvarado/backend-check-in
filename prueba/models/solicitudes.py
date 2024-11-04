from django.db import models
from django.core.exceptions import ValidationError

class SolicitudJustificante(models.Model):
    """
    Modelo de Justificante
    """
    OPCIONES_ESTADO = [
        ('A', 'Aprobada'),
        ('R', 'Rechazada'),
        ('P', 'Pendiente'),
    ]    
    estado_solicitud =  models.CharField(max_length=1,choices=OPCIONES_ESTADO,default='P',)

    motivo = models.CharField(max_length=150,null=True,blank=True,help_text='Motivo por la cual se va a justificar')
    
    dia_justificar = models.DateField(null=True,blank=True,help_text='Dia que quiere justificar')
    
    clave_empleado = models.IntegerField(null=True,blank=True,help_text='Clave del empleado que quiere justificar')
    
    evidencia_pdf = models.FileField(null=True, blank=True ,upload_to='documentos_pdfs/')

    usuario_que_registra = models.ForeignKey("prueba.Usuario",
                                             null=True,
                                             blank=True,
                                             related_name='solicitudes_justificantes',
                                             help_text='Relacion al empleaod que hizo el justificante, se va a relacionar con la clave que se ortorga ',
                                             on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'solicitudes_justificantes'
        ordering = ['pk']
        verbose_name = 'Solicitud de justificante'
        verbose_name_plural = 'Solicitudes de justificantes'
        permissions = [
            ['autorizar_solicitudjustificane', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_solicitudjustificane', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def clean(self):
        super().clean()
        if self.evidencia_pdf:
            if not self.evidencia_pdf.name.endswith('.pdf'):
                raise ValidationError("El archivo debe ser un PDF.")

    def __str__(self):
        return f"Pk: {self.pk} | Estado De Solicitud: {self.estado_solicitud} | Clave Usuario: {self.clave_empleado} | Día a Justificar: {self.dia_justificar}"
