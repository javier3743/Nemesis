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

    path('RA/<int:pk>',  RAList.as_view(), name= 'landingRA'),
    path('addRA/<int:pk>',  RACreate.as_view(), name= 'addRA'),
    path('updateRA/<int:pk>',  RAUpdate.as_view(), name= 'updateRA'),
    path('deleteRA/<int:pk>',  RADelete.as_view(), name= 'deleteRA'),

    path('landingIL/<int:pk>',  ILList.as_view(), name= 'landingIL'),
    path('addIL/<int:pk>',  ILCreate.as_view(), name= 'addIL'),
    path('updateIL/<int:pk>',  ILUpdate.as_view(), name= 'updateIL'),
    path('deleteIL/<int:pk>',  ILDelete.as_view(), name= 'deleteIL'),

    path('landingADF/<int:pk>', ADFList.as_view(), name='landingADF'),
    path('addADF/<int:pk>', ADFCreate.as_view(), name='addADF'),
    path('updateADF/<int:pk>', ADFUpdate.as_view(), name='updateADF'),
    path('deleteADF/<int:pk>', ADFDelete.as_view(), name='deleteADF'),

    path('landingADE/<int:pk>', ADEList.as_view(), name='landingADE'),
    path('addADE/<int:pk>', ADECreate.as_view(), name='addADE'),
    path('updateADE/<int:pk>', ADEUpdate.as_view(), name='updateADE'),
    path('deleteADE/<int:pk>', ADEDelete.as_view(), name='deleteADE'),
]
