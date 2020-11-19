from django.db import models
from django.urls import reverse
from datetime import datetime

from usuario.models import Solicitante, Interprete, Persona
from especialidad.models import Especialidad

# Create your models here.
class Atencion(models.Model):
    ATENCION_STATE_CHOICES = ((0, 'solicitado'), (1, 'aceptado'), (2, 'confirmado'), (3, 'sesion'), (4, 'finalizado'), (5, 'cancelado'))

    # FK
    solicitante = models.ForeignKey(Solicitante, on_delete=models.DO_NOTHING, related_name='atenciones')
    interprete = models.ForeignKey(Interprete, on_delete=models.DO_NOTHING, related_name='atenciones', null=True, blank=True)
    # Datos de la atencion
    especialidad = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING, related_name='atenciones')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    duracion = models.DecimalField(max_digits = 3 ,decimal_places = 1, default = 0.5)
    # TODO Modulo reserva 
    fecha_reserva = models.DateTimeField(blank=True, null=True)
    # Metadatos de procesos
    fecha_inicio_sesion = models.DateTimeField(blank=True, null=True)
    fecha_termino = models.DateTimeField(blank=True, null=True)
    estado = models.PositiveSmallIntegerField(choices=ATENCION_STATE_CHOICES, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'atenciones'

    def get_absolute_url(self):
        return reverse('detalle_atencion', kwargs={'id': self.pk}) 
        #return reverse('listado_atenciones')

    def __str__(self):
        return f'Atencion #{self.pk} - {self.titulo}'

    def aceptar(self, interprete):
        """
            Cambia el estado de la atención actual

            interprete (Interprete) - El interprete que realiza la atencion
        """

        self.interprete = interprete
        # self.fecha_atencion = datetime.now()
        self.estado = 1
        self.save()

    def confirmar(self):
        # TODO logica de cobro
        self.estado = 2
        self.save()

    def iniciar_sesion(self):
        # TODO logica inicio sesion
        self.estado = 3
        self.save()

    def finalizar(self):
        """
            Termina la atencion, finalizando su estado
        """

        self.estado = 4
        self.fecha_termino = datetime.now()
        self.save()

    def cancelar(self):
        self.estado = 5
        self.save()

    def esta_finalizada(self):
        return self.estado == 4
            
class Sesion(models.Model):
    sesion_id = models.IntegerField()
    atencion = models.OneToOneField(Atencion, on_delete=models.CASCADE, related_name='sesion')
    host_url = models.URLField(verbose_name='Link para iniciar')
    join_url = models.URLField(verbose_name='Link para unirse')

    def terminar_sesion(self):
        self.atencion.fecha_termino = datetime.now()
        self.atencion.save()