from rest_framework import serializers
from apps.usuarios.models import Idioma

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = ['nombre', 'codigo']
