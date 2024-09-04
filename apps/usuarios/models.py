from django.db import models

# Create your models here.

class Idioma(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    codigo = models.CharField(verbose_name="Codigo", max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "usuarios.Idioma"  # Define el nombre de la tabla en la base de datos
        verbose_name = "Idioma"  # Define el nombre singular del modelo para la interfaz de administración
        verbose_name_plural = "Idiomas"  # Define el nombre plural del modelo para la interfaz de administración

class Nacionalidad(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    codigo = models.CharField(verbose_name="Codigo", max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "usuarios.Nacionalidad"  # Define el nombre de la tabla en la base de datos
        verbose_name = "Nacionalidad"  # Define el nombre singular del modelo para la interfaz de administración
        verbose_name_plural = "Nacionalidades"  # Define el nombre plural del modelo para la interfaz de administración

class TipoDeCuenta(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "usuarios.TipoDeCuenta"  # Define el nombre de la tabla en la base de datos
        verbose_name = "TipoDeCuenta"  # Define el nombre singular del modelo para la interfaz de administración
        verbose_name_plural = "TiposDeCuentas"  # Define el nombre plural del modelo para la interfaz de administración

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo_electronico = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=20)
    tipo_de_cuenta = models.ForeignKey(TipoDeCuenta, on_delete=models.CASCADE, null=True, blank=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "usuarios.Usuario"  # Define el nombre de la tabla en la base de datos
        verbose_name = "Usuario"  # Define el nombre singular del modelo para la interfaz de administración
        verbose_name_plural = "Usuarios"  # Define el nombre plural del modelo para la interfaz de administración

