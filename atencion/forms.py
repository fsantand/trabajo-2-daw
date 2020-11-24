from django import forms
from .models import Atencion
from .widgets import BootstrapDateTimePickerInputCreate,BootstrapDateTimePickerInputModify

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Atencion
        exclude = ['fecha_inicio_sesion', 'fecha_termino', 'estado']
        widgets = {
            'solicitante' : forms.HiddenInput(),
            'interprete' : forms.HiddenInput(),
            'fecha_creacion' : forms.HiddenInput(),
            'fecha_reserva' : BootstrapDateTimePickerInputCreate(),
        }

    def __init__(self, *args, **kwargs):
        especialidades = kwargs.pop('especialidades')
        super(SolicitudForm, self).__init__(*args, **kwargs)
        self.fields['especialidad'].queryset = especialidades

class ModificarForm(forms.ModelForm):
    class Meta:
        model = Atencion
        exclude = ['fecha_inicio_sesion', 'fecha_termino', 'solicitante', 'interprete', 'estado']
        widgets = {
            'fecha_reserva': BootstrapDateTimePickerInputModify(),
        }


