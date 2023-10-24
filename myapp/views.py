from cmath import log
from csv import reader
from email import message
import imp
from pyexpat.errors import messages
from turtle import title
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .models import crearCurso
from .forms import crearCursoForms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

desarrollado = 'Estudiantes Ingenieria de Software - Universidad Cooperativa de Colombia '


def index(request):
    return render(request, 'index.html', {
        'desarrollado': desarrollado
    })

@login_required
def signout(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'desarrollado': desarrollado
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'usuario o contraseña incorrectos',
                'desarrollado': desarrollado
            })
        else:
            login(request, user)
            return index(request)
        

@login_required
def crearCursos(request):
    us = request.user.username
    cursos = crearCurso.objects.all()
    # print(us)
    if request.method == 'GET':
        
        return render(request, 'courses/forms/create.html', {
            'form': crearCursoForms(),
            'cursos': cursos,
        })
    else:
        crearCurso.objects.create(idCurso=request.POST['idCourse'], nombreCurso=request.POST['nombreCurso'], numeroCreditos=request.POST['numeroCreditos'], tipoPrograma=request.POST['tipoPrograma'], programaPertenece=request.POST['programaPertenece'], semestre=request.POST['semestre'], descripcion=request.POST['descripcion'])
        return index(request)

def profile(request):
    return render(request, 'profile/profile.html', {
        'desarrollado': desarrollado,
    })