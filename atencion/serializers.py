from rest_framework import serializers

from .models import Atencion, Sesion

class AtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atencion
        fields = ['pk', 'titulo', 'descripcion', 'especialidad', 'duracion', 'interprete', 'solicitante']