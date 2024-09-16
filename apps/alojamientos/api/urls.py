from rest_framework import routers

from .api import TipoAlojamientoViewset, TipoHabitacionViewset, AlojamientoViewset

router = routers.DefaultRouter()

router.register('api/TiposAlojamientos', TipoAlojamientoViewset, 'TiposAlojamientos')
router.register('api/TiposHabitaciones', TipoHabitacionViewset, 'TiposHabitaciones')
router.register('api/Alojamientos', AlojamientoViewset, 'Alojamientos')


urlpatterns = router.urls