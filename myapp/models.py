from email.policy import default
from random import choices
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

class crearCurso(models.Model):
    idCurso = models.CharField(max_length=10)
    nombreCurso = models.CharField(max_length=30)
    numeroCreditos = models.CharField(max_length=3)
    tipoPrograma = models.CharField(max_length=10)
    programaPertenece = models.CharField(max_length=30)
    semestre = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=200)
