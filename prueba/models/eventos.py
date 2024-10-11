from django.db import models

class Evento(models.Model):
    """
    Modelo de eventos
    """
    nombre_del_rentador = models.CharField(max_length=255,
                            null=True,
                            blank=True)
    
    numero_de_celular_rentador = models.BigIntegerField(null=True, 
                                                        blank=True, 
                                                        help_text='Número de teléfono del usuario')
    
    #TODO: Trabajar a fututo sobre que bloque se va a rentear al cliente
    # bloque = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    
    pago_renta = models.BooleanField(default=False)
    
    fecha_de_evento = models.DateField(null=True, 
                                       blank=True, 
                                       help_text='Indica la fecha del eventp')
    
    observaciones = models.TextField(null=True, 
                                     blank=True, 
                                     help_text='Indica cualquier información referente al evento')

    class Meta:
        db_table = 'eventos'
        ordering = ['pk']
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        permissions = [
            ['autorizar_evento', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_evento', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Nombre Del Rentador: {self.nombre_del_rentador} | Fecha: {self.fecha_de_evento}"
