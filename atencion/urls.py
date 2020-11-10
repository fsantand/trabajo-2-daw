from django.urls import path
from . import views

urlpatterns = [
    path('solicitar/<interprete>', views.SolicitudView.as_view(), name="solicitar_atencion"),
    path('detalle/<int:id>', views.detalleAtencion, name="detalle_atencion"),
    path('listado',views.listadoAtenciones, name="listado_atenciones")
]