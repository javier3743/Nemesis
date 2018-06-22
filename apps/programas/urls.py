from django.urls import path
from apps.programas.views import *

urlpatterns = [
    path('', AllProgramas.as_view(), name='landingProgramas'),
    path('add', ProgramaCreate.as_view(), name='addPrograma'),
    path('delete/<int:pk>', ProgramaDelete.as_view(), name='deletePrograma'),
    path('update/<int:pk>', ProgramaUpdate.as_view(), name='updatePrograma'),
]
