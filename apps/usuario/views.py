from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.usuario.forms import RegistroForm

# Create your views here.

def ver_datos(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST)
				
	return HttpResponse(request)
	#else:
	#	form = MascotaForm()
	#return render(request, 'mascota/mascota_form.html', {'form':form})

	#if request.method == 'POST':
	#	form = MascotaForm(request.POST)
	#	if form.is_valid():
	#		form.save()
	#	return redirect('mascota_listar')
	#else:
	#	form = MascotaForm()
	#return render(request, 'mascota/mascota_form.html', {'form':form})

class RegistroUsuario(CreateView):	
	model = User
	template_name = "usuario/registrar.html"	
		#form_class = UserCreationForm
	form_class = RegistroForm
	#success_url = reverse_lazy('auto_listar')
