from rest_framework import routers

from .api import TipoEventoViewset, EventoViewset

router = routers.DefaultRouter()

router.register('api/TiposEventos', TipoEventoViewset, 'TiposEventos')
router.register('api/Eventos', EventoViewset, 'Eventos')

urlpatterns = router.urls