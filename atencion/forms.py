from django import forms
from .models import Atencion

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Atencion
        exclude = ['interprete', 'fecha_atencion', 'fecha_termino', 'estado']
        widgets = {'solicitante': forms.HiddenInput()}
    
    def save(self, user = None):
        solicitud = super(SolicitudForm, self).save(commit=False)
        solicitante = None
        if user:
            if user.solicitante:
                solicitante = user.solicitante
        solicitud.solicitante = solicitante
        solicitud.save()
        return solicitud