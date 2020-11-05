from django.test import TestCase
from .models import Atencion
from especialidad.models import Especialidad
from usuario.models import Interprete, Solicitante

class AtencionTestCase(TestCase):
    def setUp(self):
        Especialidad.objects.create(especialidad='Ofimatica')
        Interprete.objects.create(rut='19136636', dv='0',
            nombres='Federico Andrés',
            apellido_paterno='Santander',
            apellido_materno='Lazcano',
            telefono='87755766',
            correo='federicosantander95@gmail.com',
            biografia='',
            calificacion=0,
            esta_verificado=True,
            tiempo_experiencia=2,
            especialidades=[Especialidad.objects.get(especialidad='Ofimatica')]
        )

    def test_aceptar_atencion(self):
        self.assertTrue(False)