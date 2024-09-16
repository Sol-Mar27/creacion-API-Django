from rest_framework import routers

from .api import MenuViewset, RestauranteViewset, RestauranteMenuViewset

router = routers.DefaultRouter()

router.register('api/menus', MenuViewset, 'menus')
router.register('api/restaurantes', RestauranteViewset, 'restaurantes')
router.register('api/restaurantes_menus', RestauranteMenuViewset, 'restaurantes_menus')


urlpatterns = router.urls