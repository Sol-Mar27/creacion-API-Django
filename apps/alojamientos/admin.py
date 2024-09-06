from django.contrib import admin
from apps.alojamientos.models import *

# Register your models here.

admin.site.register(TipoAlojamiento)
admin.site.register(TipoHabitacion)
admin.site.register(Alojamiento)