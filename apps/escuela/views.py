from django.shortcuts import render
from apps.usuarios.decorators import *
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import *
from apps.programas.forms import *

@method_decorator([login_required, dean_required], name='dispatch')
class AllEscuelas(ListView):
    model = Escuela
    template_name = 'programas/landingEscuelas.html'

@method_decorator([login_required, dean_required], name='dispatch')
class EscuelaCreate(CreateView):
    model = Escuela
    form_class = EscuelaFrom
    template_name = 'programas/addEscuela.html'
    success_url = '/escuelas'

@method_decorator([login_required, dean_required], name='dispatch')
class EscuelaDelete(DeleteView):
    model = Escuela
    template_name = 'programas/deleteEscuela.html'
    success_url = '/escuelas'

@method_decorator([login_required, dean_required], name='dispatch')
class EscuelaUpdate(UpdateView):
    model = Escuela
    form_class = EscuelaFrom
    template_name = 'programas/addPrograma.html'
    success_url = '/escuelas'

@method_decorator([login_required, dean_required], name='dispatch')
class FacultadCreate(CreateView):
    model = Facultad
    form_class = FacultadFrom
    template_name =  'programas/addFacultad.html'
    success_url = '/escuelas'