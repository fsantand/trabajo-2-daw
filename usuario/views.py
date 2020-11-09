from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

from .models import Interprete, Solicitante
from .forms import RegisterForm

# Create your views here.
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_user = request.POST.get('remember', False)

        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            if not remember_user:
                request.session.set_expiry(0)
            messages.success(request, 'Estas conectado ahora !')
            return redirect('dash')
        else:
            messages.error(request, 'Credenciales inexistentes o erroneas')
            return redirect('login')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dash')
        else:    
            return render(request, 'usuario/login.html')
        
@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required
def dash(request):
    if hasattr(request.user,"interprete"):
        return render(request, 'usuario/interprete/peticionesActivas.html',{})
    else:
        return render(request, 'usuario/solicitante/solicitarInterprete.html',{})

@login_required
def solicitarInterprete(request):
    if hasattr(request.user,"solicitante"):
        return render(request, 'usuario/solicitante/solicitarInterprete.html',{})
    else:
        messages.error(request, 'No posee acceso a dicha ruta')
        return render(request, 'usuario/interprete/peticionesActivas.html',{})
    
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Crear usuario
            new_user, created = User.objects.get_or_create(
                username=form.cleaned_data['usuario'],
                email=form.cleaned_data['correo']
            )
            if created:
                new_user.set_password(raw_password = form.cleaned_data['password'])
                new_user.save()
                tipo_usuario = form.cleaned_data['tipo_usuario']
                rut, dv = form.cleaned_data['rut']
                if tipo_usuario == 'cliente':
                    print ('Tipo de usuario es cliente !')
                    new_cliente = Solicitante.objects.create(
                        usuario=new_user,
                        rut=rut,
                        dv=dv,
                        nombres=form.cleaned_data['nombres'],
                        apellido_paterno=form.cleaned_data['apellido_paterno'],
                        apellido_materno=form.cleaned_data['apellido_materno'],
                        telefono=form.cleaned_data['telefono'],
                        correo=form.cleaned_data['correo'],
                        biografia=form.cleaned_data['biografia']
                    )
                elif tipo_usuario == 'interprete':
                    print ('Tipo de usuario es interprete !')
                    new_interprete = Interprete.objects.create(
                        usuario=new_user,
                        rut=rut,
                        dv=dv,
                        nombres=form.cleaned_data['nombres'],
                        apellido_paterno=form.cleaned_data['apellido_paterno'],
                        apellido_materno=form.cleaned_data['apellido_materno'],
                        telefono=form.cleaned_data['telefono'],
                        correo=form.cleaned_data['correo'],
                        biografia=form.cleaned_data['biografia'],
                        esta_verificado=False,
                        tiempo_experiencia=0
                    )
            # Asignar tipo usuario
                return redirect('login')
    return render(request, 'usuario/signup.html', {'form': RegisterForm()})