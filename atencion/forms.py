from django import forms
from .models import Atencion

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Atencion
        exclude = ['fecha_inicio_sesion', 'fecha_termino', 'estado']
        widgets = {
            'solicitante' : forms.HiddenInput(),
            'interprete' : forms.HiddenInput(),
            'fecha_creacion' : forms.HiddenInput(),
            'fecha_reserva' : forms.TextInput(attrs={'type': 'date'}),
        }

    
    def __init__(self, *args, **kwargs):
        especialidades = kwargs.pop('especialidades')
        super(SolicitudForm, self).__init__(*args, **kwargs)
        self.fields['especialidad'].queryset = especialidades
      
    # def save(self, user = None):
    #     solicitud = super(SolicitudForm, self).save(commit=False)
    #     solicitante = None
    #     if user:
    #         if user.solicitante:
    #             solicitante = user.solicitante
    #     solicitud.solicitante = solicitante
    #     solicitud.save()
    #     return solicitud