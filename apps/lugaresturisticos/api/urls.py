from rest_framework import routers
from .api import LugarTuristicoViewset

router = routers.DefaultRouter()

router.register('api/LugaresTuristico', LugarTuristicoViewset, 'LugaresTuristicos')


urlpatterns = router.urls
