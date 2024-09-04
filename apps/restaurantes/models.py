from django.db import models

# Create your models here.

class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "restaurantes.Menu"  # Define el nombre de la tabla en la base de datos
        verbose_name = "Menu"  # Define el nombre singular del modelo para la interfaz de administración
        verbose_name_plural = "Menus"  # Define el nombre plural del modelo para la interfaz de administración 

class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    latitud = models.FloatField()
    longitud = models.FloatField()
    imagen = models.ImageField(upload_to='media/imagenes/')
    estado = models.BooleanField(default=True)
    hora_apertura = models.DateField()
    hora_cierre = models.DateField()
