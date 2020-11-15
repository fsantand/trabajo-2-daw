from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import SolicitudForm
from .models import Atencion
from usuario.models import Interprete
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class SolicitudView(LoginRequiredMixin,CreateView):
    model = Atencion
    template_name = 'atencion/solicitar.html'
    form_class = SolicitudForm

    
    # def __init__(self, **kwargs):
    #     super(SolicitudView, self).__init__(**kwargs)
    #     self.interprete = kwargs['interprete']

    def get_form_kwargs(self):
        kwargs = super(SolicitudView, self).get_form_kwargs()
        rut_interprete = self.kwargs.get('interprete')
        especialidades = Interprete.objects.get(rut=rut_interprete).especialidades.all()
        kwargs['especialidades'] = especialidades
        return kwargs

    def get_initial(self):
        return {'interprete':self.kwargs.get('interprete'),'solicitante':self.request.user.solicitante}

    def get_context_data(self, **kwargs):
        ctx = super(SolicitudView, self).get_context_data(**kwargs)
        u_interprete = Interprete.objects.get(rut=self.kwargs['interprete'])
        ctx['interprete'] = u_interprete
        return ctx

    def form_valid(self, form):
        form.save(self.request.user)
        return super(SolicitudView, self).form_valid(form)

    


def detalleAtencion(request):
    return render(request, 'atencion/detalleAtencion.html',{})

def listadoAtenciones(request):
    ctx = {}
    if request.method == 'GET':
        atenciones = request.user.solicitante.atenciones.exclude(estado=5)
        ctx['listaAtenciones'] = atenciones
        return render(request, 'atencion/atenciones.html',ctx)
    if request.method == 'POST':
        id_atencion = request.POST['id']
        if 'view' in request.POST:
            pass
        if 'edit' in request.POST:
            pass
        if 'delete' in request.POST:
            atencion = Atencion.objects.get(id=id_atencion)
            atencion.cancelar()
            return redirect('listado_atenciones')

    