from django.urls import path, include
from . import views

urlpatterns = [
    path('atencion/', include('atencion.api'))
]