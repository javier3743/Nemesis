from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from apps.cursos.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from apps.usuarios.decorators import *
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.http import request


# Create your views here.
@method_decorator([login_required, cursos_required], name='dispatch')
class AllCourses(ListView):
    model = Curso
    template_name = 'cursos/landingCursos.html'


@method_decorator([login_required, cursos_required], name='dispatch')
class CursoCreate(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/addCursos.html'
    success_url = '/cursos'


@method_decorator([login_required, cursos_required], name='dispatch')
class CursoDelete(DeleteView):
    model = Curso
    template_name = 'cursos/deleteCursos.html'
    success_url = '/cursos'


@method_decorator([login_required, cursos_required], name='dispatch')
class CursoUpdate(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/addCursos.html'
    success_url = '/cursos'


class CursoDesign(ListView):
    model = Competencias
    template_name = 'cursos/landingCompe.html'

    def get_context_data(self, **kwargs):
        this_name = self.kwargs['pk']
        context = super(CursoDesign, self).get_context_data(**kwargs)
        context['tags'] = Curso.objects.get(pk= this_name)
        return context

class CompetenciaCreate(CreateView):
    model = Competencias
    form_class = CompeForm
    template_name = 'cursos/addCompe.html'

    def get_success_url(self):
        return reverse('designCurso', kwargs={'pk' : self.kwargs['pk']})

    def get_initial(self):
        return { 'Curso':  self.kwargs['pk']}

class CompetenciaUpdate(UpdateView):
    model = Competencias
    form_class = CompeForm
    template_name = 'cursos/addCompe.html'

    def get_success_url(self):
        return reverse('designCurso', kwargs={'pk' : Competencias.objects.values_list('Curso_id', flat= True).get(pk= self.kwargs['pk'])})

    def get_initial(self):
        return {'Competencia': Competencias.objects.values_list('Competencia', flat= True).get(pk= self.kwargs['pk']),
               'Curso': Competencias.objects.values_list('Curso_id', flat= True).get(pk= self.kwargs['pk'])}

class CompetenciaDelete(DeleteView):
    model = Competencias
    template_name = 'cursos/deleteCompe.html'

    def get_success_url(self):
        return reverse('designCurso', kwargs={'pk' : Competencias.objects.values_list('Curso_id', flat= True).get(pk= self.kwargs['pk'])})

    def get_context_data(self, **kwargs):
        this_name = self.kwargs['pk']
        context = super(CompetenciaDelete, self).get_context_data(**kwargs)
        context['Curso'] = Curso.objects.get(pk= Competencias.objects.values_list('Curso_id',flat=True).get(pk= this_name))
        context['Competencias'] = Competencias.objects.get(pk= this_name)
        return context

class RAList(ListView):
    model = ResultadoDeAprendizaje
    template_name = 'cursos/landingRA.html'

    def get_context_data(self, **kwargs):
        this_name = self.kwargs['pk']
        context = super(RAList, self).get_context_data(**kwargs)
        context['Compe'] = Competencias.objects.get(pk= this_name)
        return context

class RACreate(CreateView):
    model = ResultadoDeAprendizaje
    form_class = RAForm
    template_name = 'cursos/addRA.html'

    def get_success_url(self):
        return reverse('landingRA', kwargs={'pk': self.kwargs['pk']})

    def get_initial(self):
        return {'Competencia': self.kwargs['pk']}

class RAUpdate(UpdateView):
    model = ResultadoDeAprendizaje
    form_class = RAForm
    template_name = 'cursos/addRA.html'

    def get_success_url(self):
        return reverse('landingRA', kwargs={'pk' : ResultadoDeAprendizaje.objects.values_list('Competencia_id', flat= True).get(pk= self.kwargs['pk'])})

    def get_initial(self):
        return {'Verbo': ResultadoDeAprendizaje.objects.values_list('Verbo', flat= True).get(pk= self.kwargs['pk']),
                'Contenidos': ResultadoDeAprendizaje.objects.values_list('Contenidos', flat=True).get(pk=self.kwargs['pk']),
                'Contexto': ResultadoDeAprendizaje.objects.values_list('Contexto', flat=True).get(pk=self.kwargs['pk']),
                'Proposito': ResultadoDeAprendizaje.objects.values_list('Proposito', flat=True).get(pk=self.kwargs['pk']),
                'Competencia': ResultadoDeAprendizaje.objects.values_list('Competencia_id', flat= True).get(pk= self.kwargs['pk'])}


class RADelete(DeleteView):
    model = ResultadoDeAprendizaje
    template_name = 'cursos/deleteRA.html'

    def get_success_url(self):
        return reverse('landingRA', kwargs={'pk' : ResultadoDeAprendizaje.objects.values_list('Competencia_id', flat= True).get(pk= self.kwargs['pk'])})

    def get_context_data(self, **kwargs):
        this_name = self.kwargs['pk']
        context = super(RADelete, self).get_context_data(**kwargs)
        context['Competencias'] = Competencias.objects.get(pk= ResultadoDeAprendizaje.objects.values_list('Competencia_id',flat=True).get(pk= this_name))
        context['Resultados'] = ResultadoDeAprendizaje.objects.get(pk= this_name)
        return context







