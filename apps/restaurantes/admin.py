from django.contrib import admin
from apps.restaurantes.models import *

# Register your models here.
admin.site.register(Restaurante)
admin.site.register(Menu)
admin.site.register(RestauranteMenu)
