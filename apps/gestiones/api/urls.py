from rest_framework import routers

from .api import RedSocialViewset, ValoracionComentarioViewset

router = routers.DefaultRouter()

router.register('api/RedesSociales', RedSocialViewset, 'RedesSociales')
router.register('api/ValoracionesComentarios', ValoracionComentarioViewset, 'ValoracionesComentarios')

urlpatterns = router.urls