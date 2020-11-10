from django import forms

from .models import Review

class ReviewForm(forms.Form):
    usuario_pk = forms.IntegerField(required=True, widget=forms.HiddenInput)
    calificacion = forms.ChoiceField(choices=((1, 1),(2, 2),(3, 3),(4, 4),(5, 5)), widget=forms.RadioSelect)
    review = forms.CharField(widget=forms.Textarea)