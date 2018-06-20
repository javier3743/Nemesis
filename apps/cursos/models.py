from django.db import models
from apps.programas.models import *
from apps.usuarios.models import *

# Create your models here.

class Curso(models.Model):
    Codigo = models.CharField(max_length=50, unique= True)

    Nombre = models.CharField(max_length=50)

    Creditos = models.PositiveSmallIntegerField()

    HorasDeClaseMagistral = models.PositiveSmallIntegerField(null=True)

    NumHorasEstudio = models.PositiveSmallIntegerField(null=True)

    TiposDeCursos = (('Asignatura básica', 'Asignatura básica'), ('Asignatura Profesional', 'Asignatura Profesional'),
                     ('Electiva Complementaria', 'Electiva Complementaria'),
                     ('Electiva Profesional', 'Electiva Profesional'))
    TipoDeCurso = models.CharField(max_length=50, choices=TiposDeCursos, default='Asignatura básica')

    AsigPrerrequisitos = models.ManyToManyField("Curso", blank = True)

    EsValidable = (('Si', 'Si'), ('No', 'No'))
    Validable = models.CharField(max_length=2, choices=EsValidable, default='SI')

    EsHabilitable = (('Si', 'Si'), ('No', 'No'))
    Habilitable = models.CharField(max_length=2, choices=EsHabilitable, default='SI')

    Programa = models.ForeignKey(ProgramaAcademico, null=False, blank=False, on_delete=models.CASCADE)

    NumSemestreUbic = models.PositiveSmallIntegerField(null=True)

    Profesor = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)


    def __str__(self):
        return "{0}".format(self.Nombre)

class Competencias(models.Model):

    Competencia = models.CharField(max_length=500)
    Curso = models.ForeignKey(Curso, null=True, blank=False, on_delete=models.CASCADE)

    Estado = models.BooleanField

    def __str__(self):
        return "{0}".format(self.Competencia)

class ResultadoDeAprendizaje(models.Model):

    Verbo = models.CharField(max_length=15)
    Contenidos = models.CharField(max_length=100)
    Contexto = models.CharField(max_length=100)
    Proposito = models.CharField(max_length=100)
    Competencia = models.ForeignKey(Competencias, null=True, blank=False,  on_delete=models.CASCADE)


class IndicadoresDeLogro(models.Model):

    Habilidad = models.CharField(max_length=15)
    Contenido = models.CharField(max_length=100)
    Contexto = models.CharField(max_length=100)
    RA = models.ForeignKey(ResultadoDeAprendizaje,  null=True, blank=False, on_delete=models.CASCADE)

class ActividadesDeFormacion(models.Model):

    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=150)
    RA = models.ForeignKey(ResultadoDeAprendizaje,  null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.Nombre)


class ActividadesDeEvaluacion(models.Model):

    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=150)
    IL = models.ForeignKey(IndicadoresDeLogro,  null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.Nombre)