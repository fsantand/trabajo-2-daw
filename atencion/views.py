from django.shortcuts import render
from django.views.generic import CreateView

from .forms import SolicitudForm
from .models import Atencion

# Create your views here.
class SolicitudView(CreateView):
    model = Atencion
    template_name = 'atencion/solicitar.html'
    form_class = SolicitudForm

    def form_valid(self, form):
        form.save(self.request.user)
        return super(SolicitudView, self).form_valid(form)
