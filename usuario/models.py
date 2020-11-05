from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator
from django.conf import settings
from especialidad.models import Especialidad

# Create your models here.
class Persona(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    rut = models.CharField(
        max_length=10,
        primary_key=True,
        validators=[
            RegexValidator(r'^\d{7,8}$')
        ])
    dv = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9K]$')])
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    telefono = models.CharField(
        max_length=13,
        validators=[RegexValidator(r'^(\+56[1-9]{1,2}|)[1-9][0-9]{7}$')]
    )
    correo = models.EmailField()
    biografia = models.TextField(blank=True)
    calificacion = models.PositiveIntegerField(validators=[MaxValueValidator(5)], default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.apellido_paterno} {self.apellido_materno}, {self.nombres}'

    def get_rut(self):
        return f'{self.rut}-{self.dv}'

    def get_calificacion(self):
        pass

    def actualizar_calificacion(self):
        pass

class Solicitante(Persona):
    saldo = models.PositiveIntegerField(default=0)

class Interprete(Persona):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/no-img.jpg')
    esta_verificado = models.BooleanField()
    tiempo_experiencia = models.PositiveIntegerField()
    especialidades = models.ManyToManyField(Especialidad, related_name='interpretes')
