from django.db import models
from apps.usuarios.models import InformacionBase

class ActivoManager(models.Manager):
    def activos(self):
        return self.filter(estado=True)

class Menu(InformacionBase):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    precio = models.FloatField()  
    objects = ActivoManager()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "restaurantes.Menu"  
        verbose_name = "Menu"  
        verbose_name_plural = "Menus"
        
class Restaurante(InformacionBase):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    imagen = models.ImageField(upload_to='media/imagenes/restaurantes')
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()
    objects = ActivoManager()
    
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "restaurantes.Restaurante" 
        verbose_name = "Restaurante" 
        verbose_name_plural = "Restaurantes"  

class RestauranteMenu(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.restaurante.nombre

    class Meta:
        db_table = "restaurantes_restaurant_menu"
        verbose_name = "Restaurante Menu"
        verbose_name_plural = "Restaurantes Menus"
