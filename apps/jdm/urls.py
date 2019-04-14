from django.urls import path, include

from apps.jdm.views import index, AutoList, AutoCreate, AutoUpdate, AutoDelete

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', AutoCreate.as_view(), name='auto_crear'),
    path('listar', AutoList.as_view(), name='auto_listar'),
    path('editar/<pk>/', AutoUpdate.as_view(), name='auto_editar'),
    path('eliminar/<pk>/', AutoDelete.as_view(), name='auto_eliminar'),
]