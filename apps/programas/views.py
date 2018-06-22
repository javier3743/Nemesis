from django.shortcuts import render
from apps.usuarios.decorators import *
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.


@method_decorator([login_required, programas_required], name='dispatch')
class AllProgramas(ListView):
    model = ProgramaAcademico
    template_name = 'programas/landingProgramas.html'

@method_decorator([login_required, programas_required], name='dispatch')
class ProgramaCreate(CreateView):
    model = ProgramaAcademico
    form_class = ProgramaForm
    template_name = 'programas/addPrograma.html'
    success_url = '/programas'

@method_decorator([login_required, programas_required], name='dispatch')
class ProgramaDelete(DeleteView):
    model = ProgramaAcademico
    template_name = 'programas/deletePrograma.html'
    success_url = '/programas'

@method_decorator([login_required, programas_required], name='dispatch')
class ProgramaUpdate(UpdateView):
    model = ProgramaAcademico
    form_class = ProgramaForm
    template_name = 'programas/addPrograma.html'
    success_url = '/programas'