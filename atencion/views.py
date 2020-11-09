from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import SolicitudForm
from .models import Atencion
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class SolicitudView(LoginRequiredMixin,CreateView):
    model = Atencion
    template_name = 'atencion/solicitar.html'
    form_class = SolicitudForm

    
    def __init__(self, *args, **kwargs):
        super(SolicitudView, self).__init__(*args, **kwargs)
    

    def form_valid(self, form):
        form.save(self.request.user)
        return super(SolicitudView, self).form_valid(form)

def detalleAtencion(request):
    return render(request, 'atencion/detalleAtencion.html',{})