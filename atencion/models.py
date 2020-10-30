from django.db import models

from datetime import datetime

from usuario.models import Solicitante, Interprete, Persona
from especialidad.models import Especialidad

# Create your models here.
class Atencion(models.Model):
    ATENCION_STATE_CHOICES = ((0, 'solicitado'), (1, 'atencion'), (2, 'finalizado'))

    solicitante = models.ForeignKey(Solicitante, on_delete=models.DO_NOTHING, related_name='atenciones')
    interprete = models.ForeignKey(Interprete, on_delete=models.DO_NOTHING, related_name='atenciones')
    especialidad = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING, related_name='atenciones')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_atencion = models.DateTimeField(blank=True)
    fecha_termino = models.DateTimeField(blank=True)
    estado = models.PositiveSmallIntegerField(choices=ATENCION_STATE_CHOICES, default=0)

    class Meta:
        verbose_name_plural = 'Atenciones'

    def __str__(self):
        return f'Atencion #{self.pk} - {self.titulo}'

    def aceptar_atencion(self, interprete):
        """
            Cambia el estado de la atención actual

            interprete (Interprete) - El interprete que realiza la atencion
        """

        self.interprete = interprete
        self.fecha_atencion = datetime.now()
        self.estado = 1
        self.save()

    def terminar_atencion(self):
        """
            Termina la atencion, finalizando su estado
        """

        self.estado = 2
        self.fecha_termino = datetime.now()
        pass
    