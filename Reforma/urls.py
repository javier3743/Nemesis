"""Reforma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import login, logout
from .views import index, permission

urlpatterns = [
    path('', index, name = 'home'),
   # path('admina/', admin.site.urls),
    path('programas/', include('apps.programas.urls'), name ='programas'),
    path('escuelas/', include('apps.escuela.urls'), name ='escuelas'),
    path('cursos/', include('apps.cursos.urls'), name='curso'),
    path('admin/',include('apps.usuarios.urls'), name = 'usuarios'),
    path('login/', login, {'template_name': 'login.html'}, name='login'),
    path('logout/', logout, {'template_name':'index.html'}, name = 'logout'),
    path('permission/', permission, name ='bad' )

]
