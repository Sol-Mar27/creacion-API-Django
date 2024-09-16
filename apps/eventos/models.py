from django.db import models
from apps.usuarios.models import InformacionBase

# Create your models here.
class ActivoManager(models.Manager):
    def activos(self):
        return self.filter(estado=True)

class TipoEvento(InformacionBase):
    nombre = models.CharField(max_length=100, unique=True)
    objects = ActivoManager()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "eventos.TipoEvento" 
        verbose_name = "TipoEvento" 
        verbose_name_plural = "TiposEventos"

class Evento(InformacionBase):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    imagen = models.ImageField(upload_to='media/imagenes/eventos')
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)
    precio = models.FloatField()
    objects = ActivoManager()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "eventos.Evento" 
        verbose_name = "Evento" 
        verbose_name_plural = "Eventos" 