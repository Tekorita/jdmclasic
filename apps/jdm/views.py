from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.jdm.forms import AutoForm
from apps.jdm.models import Auto
# Create your views here.

def index(request):
    return render(request,'auto/index.html')

class AutoList(ListView):
    model = Auto
    template_name = 'auto/auto_list.html'

class AutoCreate(CreateView):
    model = Auto
    form_class = AutoForm
    template_name = 'auto/auto_form.html'
    success_url = reverse_lazy('auto_listar')

class AutoUpdate(UpdateView):
    model = Auto
    form_class = AutoForm
    template_name = 'auto/auto_form.html'
    success_url = reverse_lazy('auto_listar')

class AutoDelete(DeleteView):
    model = Auto
    template_name = 'auto/auto_delete.html'
    success_url = reverse_lazy('auto_listar')


