from django.db import models
from apps.usuarios.models import InformacionBase

# Create your models here.
class ActivoManager(models.Manager):
    def activos(self):
        return self.filter(estado=True)

class TipoAlojamiento(InformacionBase):
    nombre = models.CharField(max_length=100, unique=True)
    objects = ActivoManager()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "alojamientos.TipoAlojamiento" 
        verbose_name = "TipoAlojamiento" 
        verbose_name_plural = "TipoAlojamientos" 

class TipoHabitacion(InformacionBase):
    nombre = models.CharField(max_length=100, unique=True)
    objects = ActivoManager()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "alojamientos.TipoHabitacion" 
        verbose_name = "TipoHabitacion" 
        verbose_name_plural = "TiposHabitaciones" 
    

class Alojamiento(InformacionBase):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    imagen = models.ImageField(upload_to='media/imagenes/alojamientos')
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()
    tipo_alojamiento = models.ForeignKey(TipoAlojamiento, on_delete=models.CASCADE, null=True, blank=True)
    tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE, null=True, blank=True)
    precio = models.FloatField()
    objects = ActivoManager()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "alojamientos.Alojamiento" 
        verbose_name = "Alojamiento" 
        verbose_name_plural = "Alojamientos" 