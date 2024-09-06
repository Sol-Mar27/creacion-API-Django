from django.urls import path
from .views import IdiomaListCreate, IdiomaDetail

urlpatterns = [
    path('idiomas/', IdiomaListCreate.as_view(), name='idiomas-list-create'),
    path('idiomas/<int:pk>/', IdiomaDetail.as_view(), name='idiomas-detail'),
]