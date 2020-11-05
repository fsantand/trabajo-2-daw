from django.urls import path
from . import views

urlpatterns = [
    path('solicitar', views.SolicitudView.as_view(), name="solicitar_atencion")
]