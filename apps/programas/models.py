from django.db import models

# Create your models here.
# FACULTAD
class Facultad(models.Model):
    Nombre = models.CharField(max_length=50, unique = True)

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.Nombre)

class Escuela(models.Model):
    Nombre = models.CharField(max_length=15)
    Facultad = models.ForeignKey(Facultad, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.Nombre)

# PROGRAMA ACADEMICO
class ProgramaAcademico(models.Model):
    Codigo = models.CharField(max_length= 10, null=True, unique= True)
    Nombre = models.CharField(max_length=50, null=True)
    Escuela = models.CharField(max_length=50, null= True)
    NumSemestres = models.PositiveSmallIntegerField(null = True)
    NumCreditosGrad = models.PositiveSmallIntegerField(null = True)

    def __str__(self):
        return "{0}".format(self.Nombre)