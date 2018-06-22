from django import forms
from apps.programas.models import *

class EscuelaFrom(forms.ModelForm):
    class Meta:
        model = Escuela

        fields = [
            'Nombre',
            'Facultad',
        ]
        labels = {
            'Nombre': 'Nombre',
            'Facultad': 'Facultad',
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Facultad': forms.Select(attrs={'class': 'form-control'}),
        }

class FacultadFrom(forms.ModelForm):
    class Meta:
        model = Facultad

        fields = [
            'Nombre',
        ]
        labels = {
            'Nombre': 'Nombre',
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }