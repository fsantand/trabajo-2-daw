from django import forms
from .models import Atencion

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Atencion
        exclude = ['fecha_inicio_sesion', 'fecha_termino', 'estado','fecha_reserva']
        widgets = {
            'interprete' : forms.HiddenInput(),
            'fecha_creacion' : forms.HiddenInput(),
        }
    
    def save(self, user = None):
        solicitud = super(SolicitudForm, self).save(commit=False)
        solicitante = None
        if user:
            if user.solicitante:
                solicitante = user.solicitante
        solicitud.solicitante = solicitante
        solicitud.save()
        return solicitud