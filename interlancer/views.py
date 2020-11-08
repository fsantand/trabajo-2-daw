from django.shortcuts import render
from usuario.models import Interprete
import itertools

# Create your views here.

def home(response):
    interpretes = Interprete.objects.all().order_by('-calificacion')[:6]
    iterator = itertools.count(1)
    r = [5,4,3,2,1]
    ctx = {'destacados':interpretes,'r':r,'iterator':iterator}
    return render(response, 'home/home.html', ctx)