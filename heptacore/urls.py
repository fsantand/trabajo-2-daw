from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('detalleproducto/', views.detalleProducto, name = 'detalleproducto'),
    path('signupclient/', views.signUpClient, name = 'signupclient'),

]