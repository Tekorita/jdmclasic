from django.urls import path, include

from apps.usuario.views import RegistroUsuario, ver_datos

urlpatterns = [
	path('registrar', ver_datos, name='registrar'),
	#path('registrar', RegistroUsuario.as_view(), name='registrar'),
]