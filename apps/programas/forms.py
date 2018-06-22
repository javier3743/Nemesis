from django import forms
from .models import *

class ProgramaForm(forms.ModelForm):

    class Meta:
        model = ProgramaAcademico

        fields = [
            'Codigo',
            'Nombre',
            'NumCreditosGrad',
            'NumSemestres',
            'Escuela',
        ]
        labels ={
            'Codigo': 'Codigo',
            'Nombre': 'Nombre',
            'NumCreditosGrad':'Numero de Creditos',
            'NumSemestres':'Numero de Semestres',
            'Escuela':'Escuela',
        }
        widgets= {
            'Codigo': forms.TextInput(attrs={'class':'form-control'}),
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'NumCreditosGrad': forms.TextInput(attrs={'class':'form-control'}),
            'NumSemestres': forms.TextInput(attrs={'class':'form-control'}),
            'Escuela': forms.Select(attrs={'class':'form-control'}),
        }
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