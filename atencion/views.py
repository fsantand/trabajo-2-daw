from django.shortcuts import render,redirect,reverse, get_object_or_404
from django.views.generic import CreateView,UpdateView,DetailView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from .forms import SolicitudForm,ModificarForm
from .models import Atencion, Sesion
from usuario.models import Interprete
from usuario.mixins import InterpreteRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .services import iniciar_sesion_instantanea
from .serializers import AtencionSerializer
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

    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()


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
            
def aceptar_atencion(request, pk):
    if hasattr(request.user,'interprete'):
        atencion = get_object_or_404(Atencion, pk = pk)
        if not hasattr(atencion, 'sesion') and atencion.estado == 2:
            atencion.confirmar()
            sesion = iniciar_sesion_instantanea(atencion)
            messages.success(request, 'Sesion creada con exito! Revise su correo.')
        else:
            messages.warning(request, 'Ya existe una sesión activa para esta solicitud.')
    else:
        messages.error(request, 'No tienes acceso a esta ruta.')
    return redirect('dash')

class SesionInterpreteDetalle(LoginRequiredMixin, InterpreteRequiredMixin, DetailView):
    model = Sesion
    template_name = "sesion/detalle.html"

@permission_classes((permissions.AllowAny,))
class AtencionList(APIView):
    def get(self, request, format=None):
        atenciones = Atencion.objects.all()
        serializer = AtencionSerializer(atenciones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AtencionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class AtencionDetailApi(APIView):
    def get_object(self, pk):
        try:
            return Atencion.objects.get(pk=pk)
        except Atencion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        atencion = self.get_object(pk)
        serializer = AtencionSerializer(atencion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pass