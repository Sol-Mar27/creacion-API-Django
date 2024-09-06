from django.shortcuts import render
from rest_framework import generics
from .models import Idioma
from core.serializers import IdiomaSerializer

class IdiomaListCreate(generics.ListCreateAPIView):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer

class IdiomaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer
