from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import *
from .forms import *
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from apps.usuarios.decorators import *
from django.utils.decorators import method_decorator


# Create your views here.


#@method_decorator([login_required, admin_required], name='dispatch')
class ProfesorCreate(CreateView):
    model = User
    form_class = Profesorform
    template_name = 'usuarios/addUser.html'
    success_url = '/admin'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Profesor'

        return super().get_context_data(**kwargs)


@method_decorator([login_required, admin_required], name='dispatch')
class DirectorCreate(CreateView):
    model = User
    form_class = Directorform
    template_name = 'usuarios/addUser.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Director'

        return super().get_context_data(**kwargs)


@method_decorator([login_required, admin_required], name='dispatch')
class DeanCreate(CreateView):
    model = User
    form_class = Deanform
    template_name = 'usuarios/addUser.html'
    success_url = '/admin'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Dean'

        return super().get_context_data(**kwargs)


@method_decorator([login_required, admin_required], name='dispatch')
class UserDelete(DeleteView):
    model = User
    template_name = 'usuarios/deleteUser.html'
    success_url = '/admin'


@method_decorator([login_required, admin_required], name='dispatch')
class ProfesorUpdate(UpdateView):
    model = User
    form_class = ProfesorUpdateForm
    template_name = 'usuarios/addUser.html'
    success_url = '/admin'

    def get_initial(self):
        return {'email': User.objects.values_list('email', flat= True).get(pk= self.kwargs['pk']),
                'nombre': User.objects.values_list('first_name', flat=True).get(pk=self.kwargs['pk']),
                'apellido': User.objects.values_list('last_name', flat=True).get(pk=self.kwargs['pk']),
                'escuela': User.objects.values_list('escuela', flat= True).get(pk= self.kwargs['pk']),
                }

@method_decorator([login_required, admin_required], name='dispatch')
class DirectorUpdate(UpdateView):
    model = User
    form_class = DirectorUpdateForm
    template_name = 'usuarios/addUser.html'
    success_url = '/admin'

    def get_initial(self):
        return {'email': User.objects.values_list('email', flat= True).get(pk= self.kwargs['pk']),
                'nombre': User.objects.values_list('first_name', flat=True).get(pk=self.kwargs['pk']),
                'apellido': User.objects.values_list('last_name', flat=True).get(pk=self.kwargs['pk']),
                'programa': User.objects.values_list('programa', flat= True).get(pk= self.kwargs['pk']),
                }

@method_decorator([login_required, admin_required], name='dispatch')
class DeanUpdate(UpdateView):
    model = User
    form_class = DeanUpdateForm
    template_name = 'usuarios/addUser.html'
    success_url = '/admin'

    def get_initial(self):
        return {'email': User.objects.values_list('email', flat= True).get(pk= self.kwargs['pk']),
                'nombre': User.objects.values_list('first_name', flat=True).get(pk=self.kwargs['pk']),
                'apellido': User.objects.values_list('last_name', flat=True).get(pk=self.kwargs['pk']),
                'facultad': User.objects.values_list('facultad', flat= True).get(pk= self.kwargs['pk']),
                }

@method_decorator([login_required, admin_required], name='dispatch')
class AllUsers(ListView):
    model = User
    template_name = 'usuarios/admin.html'
