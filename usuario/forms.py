from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .validators import rut_valido

user_choices = [
    ('cliente', 'Soy cliente'),
    ('interprete', 'Soy interprete')
]

class RegisterForm(forms.Form):
    usuario = forms.CharField(max_length=75, required=True)
    password = forms.CharField(label='Contraseña' ,widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)
    rut = forms.CharField(max_length=12, validators=[RegexValidator(r'[1-9]{1,2}((\.[0-9]{3}){2}|[0-9]{6})-[0-9Kk]')])
    nombres = forms.CharField(max_length=255)
    apellido_paterno = forms.CharField(max_length=255)
    apellido_materno = forms.CharField(max_length=255)
    telefono = forms.CharField(
        max_length=13,
        validators=[RegexValidator(r'^(\+56[1-9]{1,2}|)[1-9][0-9]{7}$')]
    )
    correo = forms.EmailField()
    biografia = forms.CharField(widget=forms.Textarea, required=False)
    tipo_usuario = forms.ChoiceField(label='Tipo de Servicio',choices=user_choices, widget=forms.RadioSelect, required=True)

    def clean_rut(self):
        data = self.cleaned_data['rut']
        rut, dv = data.replace('.','').split('-')
        if not rut_valido(rut, dv):
            raise ValidationError(('RUT no valido - Ingrese un rut valido'))
        return (rut, dv)

    def validate(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise ValidationError(('Contraseñas distintas - Ingrese nuevamente'))
