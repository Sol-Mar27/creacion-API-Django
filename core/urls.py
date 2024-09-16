from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.restaurantes.api.urls')),
    path('', include('apps.usuarios.api.urls')),
    path('', include('apps.lugaresturisticos.api.urls')),
    path('', include('apps.gestiones.api.urls')),
    path('', include('apps.eventos.api.urls')),
    path('', include('apps.alojamientos.api.urls'))
]
