from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Estas conectado ahora !')
            return redirect('dash')
        else:
            messages.error(request, 'Credenciales inexistentes o erroneas')
            return redirect('login')
    if request.method == 'GET':
        return render(request, 'usuario/login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required
def dash(request):
    if hasattr(request.user,"interprete"):
        return render(request, 'usuario/interpreteNav.html',{})
    else:
        return render(request, 'usuario/solicitanteNav.html',{})

    
