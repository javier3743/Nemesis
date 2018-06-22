from django.urls import path
from apps.escuela.views import *

urlpatterns = [
    path('', AllEscuelas.as_view(), name='landingProgramas'),
    path('add', EscuelaCreate.as_view(), name='addEscuela'),
    path('delete/<int:pk>', EscuelaDelete.as_view(), name='deleteEscuela'),
    path('update/<int:pk>', EscuelaUpdate.as_view(), name='updateEscuela'),
    path('facultad', FacultadCreate.as_view(), name='facultad')

]
