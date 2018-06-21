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

class ILList(ListView):
    model = IndicadoresDeLogro
    template_name = 'cursos/landingIL.html'

    def get_context_data(self, **kwargs):
        this_name = self.kwargs['pk']
        context = super(ILList, self).get_context_data(**kwargs)
        context['RA'] = ResultadoDeAprendizaje.objects.get(pk= this_name)
        return context

class ILCreate(CreateView):
    model = IndicadoresDeLogro
    form_class = ILForm
    template_name = 'cursos/addIL.html'

    def get_success_url(self):
        return reverse('landingIL', kwargs={'pk': self.kwargs['pk']})

    def get_initial(self):
        return {'RA': self.kwargs['pk']}

class ILUpdate(UpdateView):
    model = IndicadoresDeLogro
    form_class = ILForm
    template_name = 'cursos/addIL.html'

    def get_success_url(self):
        return reverse('landingIL', kwargs={'pk' : IndicadoresDeLogro.objects.values_list('RA_id', flat= True).get(pk= self.kwargs['pk'])})

    def get_initial(self):
        return {'Habilidad': IndicadoresDeLogro.objects.values_list('Habilidad', flat= True).get(pk= self.kwargs['pk']),
                'Contenido': IndicadoresDeLogro.objects.values_list('Contenido', flat=True).get(pk=self.kwargs['pk']),
                'Contexto': IndicadoresDeLogro.objects.values_list('Contexto', flat=True).get(pk=self.kwargs['pk']),
                'RA': IndicadoresDeLogro.objects.values_list('RA_id', flat= True).get(pk= self.kwargs['pk'])}


class ILDelete(DeleteView):
    model = IndicadoresDeLogro
    template_name = 'cursos/deleteIL.html'

    def get_success_url(self):
        return reverse('landingIL', kwargs={'pk' : IndicadoresDeLogro.objects.values_list('RA_id', flat= True).get(pk= self.kwargs['pk'])})

    def get_context_data(self, **kwargs):
        this_name = self.kwargs['pk']
        context = super(ILDelete, self).get_context_data(**kwargs)
        context['Resultados'] = ResultadoDeAprendizaje.objects.get(pk= IndicadoresDeLogro.objects.values_list('RA_id',flat=True).get(pk= this_name))
        context['Indicadores'] = IndicadoresDeLogro.objects.get(pk= this_name)
        return context


class ADFList(ListView):
    model = ActividadesDeFormacion
    template_name = 'cursos/landingADF.html'

    def get_context_data(self, **kwargs):
        this_name = self.kwargs['pk']
        context = super(ADFList, self).get_context_data(**kwargs)
        context['RA'] = ResultadoDeAprendizaje.objects.get(pk= this_name)
        return context

class ADFCreate(CreateView):
    model = ActividadesDeFormacion
    form_class = ADFForm
    template_name = 'cursos/addADF.html'

    def get_success_url(self):
        return reverse('landingADF', kwargs={'pk': self.kwargs['pk']})

    def get_initial(self):
        return {'RA': self.kwargs['pk']}

class ADFUpdate(UpdateView):
    model = ActividadesDeFormacion
    form_class = ADFForm
    template_name = 'cursos/addADF.html'

    def get_success_url(self):
        return reverse('landingADF', kwargs={'pk' : ActividadesDeFormacion.objects.values_list('RA_id', flat= True).get(pk= self.kwargs['pk'])})

    def get_initial(self):
        return {'Nombre': ActividadesDeFormacion.objects.values_list('Nombre', flat= True).get(pk= self.kwargs['pk']),
                'Descripcion': ActividadesDeFormacion.objects.values_list('Descripcion', flat=True).get(pk=self.kwargs['pk']),
                'RA': ActividadesDeFormacion.objects.values_list('RA_id', flat= True).get(pk= self.kwargs['pk'])}

class ADFDelete(DeleteView):
    model = ActividadesDeFormacion
    template_name = 'cursos/deleteADF.html'

    def get_success_url(self):
        return reverse('landingADF', kwargs={'pk' : ActividadesDeFormacion.objects.values_list('RA_id', flat= True).get(pk= self.kwargs['pk'])})

    def get_context_data(self, **kwargs):
        this_name = self.kwargs['pk']
        context = super(ADFDelete, self).get_context_data(**kwargs)
        context['Resultados'] = ResultadoDeAprendizaje.objects.get(pk= ActividadesDeFormacion.objects.values_list('RA_id',flat=True).get(pk= this_name))
        context['Actividad'] = ActividadesDeFormacion.objects.get(pk= this_name)
        return context

class ADEList(ListView):
    model = ActividadesDeEvaluacion
    template_name = 'cursos/landingADF.html'

    def get_context_data(self, **kwargs):
        this_name = self.kwargs['pk']
        context = super(ADEList, self).get_context_data(**kwargs)
        context['IL'] = IndicadoresDeLogro.objects.get(pk= this_name)
        return context

class ADECreate(CreateView):
    model = ActividadesDeEvaluacion
    form_class = ADEForm
    template_name = 'cursos/addADE.html'

    def get_success_url(self):
        return reverse('landingADE', kwargs={'pk': self.kwargs['pk']})

    def get_initial(self):
        return {'RA': self.kwargs['pk']}

class ADEUpdate(UpdateView):
    model = IndicadoresDeLogro
    form_class = ADEForm
    template_name = 'cursos/addIL.html'

    def get_success_url(self):
        return reverse('landingADF', kwargs={'pk' : ActividadesDeFormacion.objects.values_list('RA_id', flat= True).get(pk= self.kwargs['pk'])})

    def get_initial(self):
        return {'Nombre': ActividadesDeFormacion.objects.values_list('Nombre', flat= True).get(pk= self.kwargs['pk']),
                'Descripcion': ActividadesDeFormacion.objects.values_list('Descripcion', flat=True).get(pk=self.kwargs['pk']),
                'RA': ActividadesDeFormacion.objects.values_list('RA_id', flat= True).get(pk= self.kwargs['pk'])}

class ADEDelete(DeleteView):
    model = IndicadoresDeLogro
    template_name = 'cursos/deleteADE.html'

    def get_success_url(self):
        return reverse('landingADE', kwargs={'pk' : ActividadesDeFormacion.objects.values_list('RA_id', flat= True).get(pk= self.kwargs['pk'])})

    def get_context_data(self, **kwargs):
        this_name = self.kwargs['pk']
        context = super(ADEDelete, self).get_context_data(**kwargs)
        context['Resultados'] = ResultadoDeAprendizaje.objects.get(pk= ActividadesDeFormacion.objects.values_list('RA_id',flat=True).get(pk= this_name))
        context['Actividad'] = ActividadesDeFormacion.objects.get(pk= this_name)
        return context