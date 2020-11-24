from django.urls import path
from . import views

urlpatterns = [
    path('', views.AtencionList.as_view()),
    path('<int:pk>', views.AtencionDetailApi.as_view())
]