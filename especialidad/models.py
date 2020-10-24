from django.db import models

# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Especialidades'
    
    def __str__(self):
        return self.especialidad