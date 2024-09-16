from rest_framework import serializers
from apps.alojamientos.models import TipoAlojamiento, TipoHabitacion, Alojamiento

class TipoAlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAlojamiento
        fields = ['id', 'nombre', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        #campos de solo lectura
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'estado', )
        
class TipoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = ['id', 'nombre', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        #campos de solo lectura
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'estado', )

class AlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alojamiento
        fields = ['id', 'nombre', 'descripcion', 'direccion', 'latitud', 'longitud', 'imagen', 'hora_apertura', 'hora_cierre', 'tipo_alojamiento', 'tipo_habitacion', 'precio', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        #campos de solo lectura
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'estado', )
        
