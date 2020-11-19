from django.urls import path
from . import views

urlpatterns = [
    path('solicitar/<interprete>', views.SolicitudView.as_view(), name="solicitar_atencion"),
    path('detalle/<int:id>', views.detalleAtencion, name="detalle_atencion"),
    path('modificar/<pk>', views.ModificarAtencionView.as_view(), name="modificar_atencion"),
    path('listado',views.listadoAtenciones, name="listado_atenciones"),
    path('aceptar/<int:pk>', views.aceptar_atencion, name="aceptar_atencion")
]