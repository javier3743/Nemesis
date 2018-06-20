from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from apps.programas.models import *

class Profesorform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)

    field_order = ["email", "first_name", "last_name", "password1", "password2"]

    first_name = forms.CharField(label='Nombre', widget=forms.TextInput)
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput)

    password1 = forms.CharField(
        label=("Contraseña"),
        strip=False,
        widget=forms.PasswordInput,

    )
    password2 = forms.CharField(
        label=("Confirmar Contraseña"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=("Ingresa nuevamente la Contraseña."),
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class Directorform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)

    field_order = ["email", "first_name", "last_name", "programa", "password1", "password2"]

    first_name = forms.CharField(label='Nombre', widget=forms.TextInput)
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput)
    programa = forms.ModelChoiceField(queryset=ProgramaAcademico.objects.all(), label='Programa Academico', widget=forms.Select)

    password1 = forms.CharField(
        label=("Contraseña"),
        strip=False,
        widget=forms.PasswordInput,

    )
    password2 = forms.CharField(
        label=("Confirmar Contraseña"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=("Ingresa nuevamente la Contraseña."),
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_director = True
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.programa = self.cleaned_data["programa"]
        if commit:
            user.save()
        return user


class Deanform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)

    field_order = ["email", "first_name", "last_name", "facultad","password1", "password2"]

    first_name = forms.CharField(label='Nombre', widget=forms.TextInput)
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput)
    facultad = forms.ModelChoiceField(queryset=Facultad.objects.all(), label='Facultad',
                                      widget=forms.Select)

    password1 = forms.CharField(
        label=("Contraseña"),
        strip=False,
        widget=forms.PasswordInput,

    )
    password2 = forms.CharField(
        label=("Confirmar Contraseña"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=("Ingresa nuevamente la Contraseña."),
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_dean = True
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.facultad = self.cleaned_data["facultad"]
        if commit:
            user.save()
        return user
