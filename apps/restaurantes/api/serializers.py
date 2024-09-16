from rest_framework import serializers
from apps.restaurantes.models import Menu, Restaurante, RestauranteMenu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'nombre', 'descripcion', 'precio', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        #campos de solo lectura
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'estado', )

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ['id', 'nombre', 'direccion', 'latitud', 'longitud', 'imagen', 'hora_apertura', 'hora_cierre', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        #campos de solo lectura
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'estado', )
        
class RestauranteMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestauranteMenu
        fields = ['id', 'restaurante', 'menu', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        #campos de solo lectura
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'estado', )   
