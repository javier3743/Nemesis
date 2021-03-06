from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import login, logout
from .views import *


urlpatterns = [
    path('', AllUsers.as_view(), name='admin'),
    path('profesor', ProfesorCreate.as_view(), name='profesor'),
    path('director', DirectorCreate.as_view(), name='director'),
    path('decano', DeanCreate.as_view(), name='deacano'),
    path('delete/<int:pk>', UserDelete.as_view(), name='deleteUser'),
    path('updatePro/<int:pk>', ProfesorUpdate.as_view(), name='updateProfesor'),
    path('updateDir/<int:pk>', DirectorUpdate.as_view(), name='updateDirector'),
    path('updateDea/<int:pk>', DeanUpdate.as_view(), name='updateDean'),

]
