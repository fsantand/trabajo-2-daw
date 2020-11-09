from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Interprete,Solicitante
from especialidad.models import Especialidad


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
        return redirect('solicitar_interprete')

@login_required
def solicitarInterprete(request):
    if hasattr(request.user,"solicitante"):
        if request.method == 'GET':
            filtro = request.GET.get('filtro',None)
            idfiltro = ''
            especialidades = Especialidad.objects.all()
            for esp in especialidades:
                if esp.especialidad == str(filtro):
                    idfiltro = esp.id
                    break
            if not idfiltro == '':
                interpretes = Interprete.objects.order_by('-calificacion').filter(especialidades__in=[idfiltro])
            else:
                interpretes = ''
            ctx = {'interpretes':interpretes}

            return render(request, 'usuario/solicitante/solicitarInterprete.html',ctx)
        if request.method == 'POST':
            intSolicitado = request.POST['interprete']
            return redirect('solicitar_atencion',intSolicitado)

        return render(request, 'usuario/solicitante/solicitarInterprete.html',{})
    else:
        messages.error(request, 'No posee acceso a dicha ruta')
        return render(request, 'usuario/interprete/peticionesActivas.html',{})
    
