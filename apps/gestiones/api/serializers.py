from rest_framework import serializers
from apps.gestiones.models import RedSocial, ValoracionComentario

class RedSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedSocial
        fields = ['id', 'nombre', 'url', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        #campos de solo lectura
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'estado', )

class ValoracionComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValoracionComentario
        fields = ['id', 'texto', 'valoracion', 'interacciones', 'usuario', 'lugar_turistico', 'evento', 'alojamiento', 'restaurante', 'red_social', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        #campos de solo lectura
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'estado', )
        
