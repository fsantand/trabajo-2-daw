from django.test import TestCase
from .models import Solicitante, Interprete

# Create your tests here.
class PersonaTestCase(TestCase):
    def setUp(self):
        Solicitante.objects.create(
            rut='19136636', dv='0',
            nombres='Federico Andrés',
            apellido_paterno='Santander',
            apellido_materno='Lazcano',
            telefono='87755766',
            correo='federicosantander95@gmail.com',
            biografia='',
            calificacion=0
        )
        Solicitante.objects.create(
            rut='8314921', dv='3',
            nombres='Federico Andrés',
            apellido_paterno='Santander',
            apellido_materno='Lazcano',
            telefono='+56999788544',
            correo='federicosantander95@gmail.com',
            biografia='',
            calificacion=0
        )
    
    def test_get_rut(self):
        persona1 = Solicitante.objects.get(rut='19136636')
        persona2 = Solicitante.objects.get(rut='8314921')
        self.assertEqual(persona1.get_rut(), '19136636-0')
        self.assertEqual(persona2.get_rut(), '8314921-3')

    def test_rut_dv_valido(self):
        persona1 = Solicitante.objects.get(rut='19136636')
        dv_valido = '0'
        self.assertTrue(persona1.dv == dv_valido)