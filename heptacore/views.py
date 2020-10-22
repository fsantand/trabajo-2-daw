from django.shortcuts import render

# Create your views here.

def index(response):
    return render(response, 'index.html', {})

def detalleProducto(response):
    return render(response, 'detalleProducto.html', {})

def signUpClient(response):
    return render(response, 'signUpClient.html', {})