from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('dash', views.dash, name="dash"),
]