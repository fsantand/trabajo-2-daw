from django.test import TestCase
from .models import Solicitante, Interprete
from .validators import rut_valido

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
        self.assertTrue(rut_valido('19136636','0')) # True
        self.assertTrue(rut_valido('19.136.636','0')) # True
        self.assertFalse(rut_valido('19136636','K')) # False
        self.assertTrue(rut_valido('8314921','3')) # True
        self.assertFalse(rut_valido('19136636','K')) # False
