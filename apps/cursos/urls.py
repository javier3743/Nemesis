from django.urls import path
from apps.cursos.views import *

urlpatterns = [
    path('', AllCourses.as_view(), name='landingCursos'),
    path('add', CursoCreate.as_view(), name='addCursos'),
    path('delete/<int:pk>', CursoDelete.as_view(), name='deleteCursos'),
    path('update/<int:pk>', CursoUpdate.as_view(), name='updateCurso'),
    path('design/<int:pk>', CursoDesign.as_view(), name='designCurso'),
    path('addCompe/<int:pk>', CompetenciaCreate.as_view(), name='addCompe'),
    path('updateCompe/<int:pk>', CompetenciaUpdate.as_view(), name='updateCompe'),
    path('deleteCompe/<int:pk>', CompetenciaDelete.as_view(), name='deleteCompe'),
    #path('RA/<int:pk>', )
]
