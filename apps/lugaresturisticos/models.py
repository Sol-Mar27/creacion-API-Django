from django.db import models
from apps.usuarios.models import InformacionBase

# Create your models here.
class ActivoManager(models.Manager):
    def activos(self):
        return self.filter(estado=True)

class LugarTuristico(InformacionBase):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    imagen = models.ImageField(upload_to='media/imagenes/lugares-turisticos')
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()
    objects = ActivoManager()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "lugaresturisticos.LugarTuristico" 
        verbose_name = "LugarTuristico" 
        verbose_name_plural = "LugaresTuristicos" 