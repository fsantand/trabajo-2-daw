from django.shortcuts import render,redirect,reverse
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from .forms import SolicitudForm,ModificarForm
from .models import Atencion
from usuario.models import Interprete
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

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

class ModificarAtencionView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Atencion
    template_name = 'atencion/modificarAtencion.html'
    form_class = ModificarForm
    success_message = 'La solicitud se ha modificado con éxito'
    
    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()


def detalleAtencion(request,id):
    ctx = {}
    ctx['atencion'] = Atencion.objects.get(id=id)
    ctx['r'] = [5,4,3,2,1]
    return render(request, 'atencion/detalleAtencion.html',ctx)

def listadoAtenciones(request):
    ctx = {}
    if request.method == 'GET':
        atenciones = request.user.solicitante.atenciones.exclude(estado=5)
        ctx['listaAtenciones'] = atenciones
        return render(request, 'atencion/atenciones.html',ctx)
    if request.method == 'POST':
        id_atencion = request.POST['id']
        if 'view' in request.POST:
            return redirect('detalle_atencion',id_atencion)
        if 'edit' in request.POST:
            return redirect('modificar_atencion',id_atencion)
        if 'delete' in request.POST:
            atencion = Atencion.objects.get(id=id_atencion)
            atencion.cancelar()
            messages.success(request, 'Se ha cancelado la atención')
            return redirect('listado_atenciones')

    