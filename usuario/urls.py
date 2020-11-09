from django.urls import path
from . import views
from interlancer import views as i

urlpatterns = [
    path('home', i.home, name="home"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('dash', views.dash, name="dash"),
    path('solicitar_interprete', views.solicitarInterprete, name="solicitar_interprete"),
    
]