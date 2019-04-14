from django.db import models
from django.urls import reverse_lazy, reverse
# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    transmision = models.CharField(max_length=50)
    año = models.IntegerField()

    def get_absolute_url(self):
	    return reverse('index')