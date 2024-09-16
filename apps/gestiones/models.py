from django.db import models
from apps.usuarios.models import InformacionBase, Usuario
from apps.restaurantes.models import Restaurante
from apps.lugaresturisticos.models import LugarTuristico
from apps.eventos.models import Evento
from apps.alojamientos.models import Alojamiento

# Create your models here. 
class ActivoManager(models.Manager):
    def activos(self):
        return self.filter(estado=True)
       
class RedSocial(InformacionBase):
    nombre = models.CharField(max_length=100, unique=True)
    url = models.URLField()
    objects = ActivoManager()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "gestiones.RedSocial" 
        verbose_name = "RedSocial"
        verbose_name_plural = "RedesSociales" 
        
class ValoracionComentario(InformacionBase):
    texto = models.TextField()
    valoracion = models.IntegerField()
    interacciones = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    lugar_turistico = models.ForeignKey(LugarTuristico, on_delete=models.CASCADE, null=True, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE, null=True, blank=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True, blank=True)
    red_social = models.ForeignKey(RedSocial, on_delete=models.CASCADE, null=True, blank=True)
    objects = ActivoManager()
    
    def __str__(self):
        return self.texto 
    
    class Meta:
        db_table = "gestiones.ValoracionComentario" 
        verbose_name = "ValoracionComentario"
        verbose_name_plural = "ValoracionesComentarios" 
    