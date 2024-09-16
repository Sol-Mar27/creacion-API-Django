from apps.lugaresturisticos.models import LugarTuristico
from rest_framework import serializers


class LugarTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LugarTuristico
        fields = ['id', 'nombre', 'descripcion', 'direccion', 'latitud', 'longitud', 'imagen', 'hora_apertura', 'hora_cierre','fecha_creacion', 'fecha_actualizacion', 'estado']
        #campos de solo lectura
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'estado', )
        
        
        
