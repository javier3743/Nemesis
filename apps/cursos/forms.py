from django import forms
from .models import *
from django_select2.forms import *


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso

        fields = [
            'Codigo',
            'Nombre',
            'Creditos',
            'HorasDeClaseMagistral',
            'NumHorasEstudio',
            'TipoDeCurso',
            'AsigPrerrequisitos',
            'Validable',
            'Habilitable',
            'Programa',
            'NumSemestreUbic',
            'Profesor',

        ]
        labels = {
            'Codigo': 'Codigo',
            'Nombre': 'Nombre',
            'Creditos': 'Creditos',
            'HorasDeClaseMagistral': 'Horas Magistrales',
            'NumHorasEstudio': 'Horas Independiente',
            'TipoDeCurso': 'Tipo de Curso',
            'AsigPrerrequisitos': 'Prerequisitos',
            'Validable': 'Validable',
            'Habilitable': 'Habilitable',
            'Programa': 'Programa Academico',
            'NumSemestreUbic': 'Ubicacion Semestral ',
            'Profesor': 'Profesor'

        }
        widgets = {
            'Codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Creditos': forms.TextInput(attrs={'class': 'form-control'},),
            'HorasDeClaseMagistral': forms.TextInput(attrs={'class': 'form-control'}),
            'NumHorasEstudio': forms.TextInput(attrs={'class': 'form-control'}),
            'TipoDeCurso': forms.Select(attrs={'class': 'form-control'}),
            'AsigPrerrequisitos': Select2MultipleWidget(),
            'Validable': forms.Select(attrs={'class': 'form-control'}),
            'Habilitable': forms.Select(attrs={'class': 'form-control'}),
            'Programa': forms.Select(attrs={'class': 'form-control'}),
            'NumSemestreUbic': forms.TextInput(attrs={'class': 'form-control'}),
            'Profesor': forms.Select(attrs={'class': 'form-control'})

        }

    def clean(self):
        cleaned_data = super(CursoForm, self).clean()
        horasMagistral = cleaned_data.get("HorasDeClaseMagistral")
        horasIndependiente = cleaned_data.get("NumHorasEstudio")
        horasSemanales = horasIndependiente + horasMagistral
        creditos = cleaned_data.get("Creditos")
        horasPermitidas = creditos * 3
        prerequisitos = cleaned_data.get("AsigPrerrequisitos")
        cod = cleaned_data.get("Codigo")
        autoPrerrequisito = prerequisitos.filter(pk=cod).exists()

        if autoPrerrequisito:
            msg = u"Un curso no puede ser prerrequisito de si mismo"
            self.add_error('prerequisitos', msg)

        if horasSemanales > horasPermitidas:
            msg = u"El número de horas de trabajo semanales excede el permitido según el número de créditos"
            self.add_error('HorasDeClaseMagistral', msg)
            self.add_error('NumHorasEstudio', msg)
            self.add_error('Creditos', msg)

        elif horasSemanales < horasPermitidas:
            msg = u"El número de horas de trabajo semanales es inferior al requerido según el número de créditos"
            self.add_error('HorasDeClaseMagistral', msg)
            self.add_error('NumHorasEstudio', msg)
            self.add_error('Creditos', msg)

class CompeForm(forms.ModelForm):
    class Meta:
        model = Competencias
        fields = ['Competencia', 'Curso']

    Competencia = forms.Field(widget=forms.Textarea(attrs={'class': 'form-control'}), label= 'Competencia')
    Curso = forms.ModelChoiceField(Curso.objects.all(), widget=forms.HiddenInput)

class RAForm(forms.ModelForm):
    class Meta:
        model = ResultadoDeAprendizaje
        fields = ['Verbo', 'Contenidos', 'Contexto', 'Proposito', 'Competencia']


    Verbo = forms.Field(widget=forms.TextInput(attrs={'class': 'form-control'}), label= 'Verbo')
    Contenidos = forms.Field(widget=forms.TextInput(attrs={'class': 'form-control'}), label= 'Contenido')
    Contexto = forms.Field(widget=forms.TextInput(attrs={'class': 'form-control'}), label= 'Contexto')
    Proposito = forms.Field(widget=forms.TextInput(attrs={'class': 'form-control'}), label= 'Proposito')
    Competencia = forms.ModelChoiceField(Competencias.objects.all(), widget=forms.HiddenInput)

