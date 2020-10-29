from django.db import models

from atencion.models import Atencion
from django.conf import settings

# Create your models here.
class Review(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    calificacion = models.PositiveIntegerField()
    review = models.CharField(verbose_name='reseña', max_length=255)
    atencion = models.ForeignKey(Atencion, on_delete = models.DO_NOTHING, related_name='reviews')

    class Meta:
        verbose_name = 'reseña'
        verbose_name_plural = 'reseñas'