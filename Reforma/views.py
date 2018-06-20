from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.usuarios.decorators import *
from django.utils.decorators import method_decorator


def index(request):
    return render(request, 'index.html')


def permission(request):
    return render(request, 'usuarios/permission.html')
