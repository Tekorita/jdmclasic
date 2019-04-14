from django import forms
from apps.jdm.models import Auto

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto

        fields = [
            'marca',
            'modelo',
            'tipo',
            'color',
            'transmision',
            'año',
        ]
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'tipo': 'Tipo',
            'color': 'Color',
            'transmision': 'Transmision',
            'año': 'Año',
        }
        widgets = {
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'transmision': forms.TextInput(attrs={'class':'form-control'}),
            'año': forms.TextInput(attrs={'class':'form-control'}),
        }
