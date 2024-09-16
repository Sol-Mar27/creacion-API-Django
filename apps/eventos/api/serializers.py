from rest_framework import serializers
from apps.eventos.models import TipoEvento, Evento

class TipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvento
        fields = ['id', 'nombre', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        #campos de solo lectura
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'estado', )

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'descripcion', 'direccion', 'latitud', 'longitud', 'imagen', 'hora_apertura', 'hora_cierre', 'tipo_evento', 'precio', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        #campos de solo lectura
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'estado', )
        
