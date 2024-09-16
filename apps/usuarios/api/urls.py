from rest_framework import routers
from .api import IdiomaViewset, NacionalidadViewSet, TipoDeCuentaViewSet, TipoDocumentoViewSet, UsuarioViewSet

router = routers.DefaultRouter()

router.register('api/idiomas', IdiomaViewset, 'idiomas')
router.register('api/nacionalidades', NacionalidadViewSet, 'nacionalidades')
router.register('api/tipos_de_cuenta', TipoDeCuentaViewSet, 'tipos_de_cuenta')
router.register('api/tipos_documentos', TipoDocumentoViewSet, 'tipos_documentos')
router.register('api/usuarios', UsuarioViewSet, 'usuarios')


urlpatterns = router.urls
