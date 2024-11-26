from django.shortcuts import render

# Create your views here.

def inicio(req):
    return render(req, 'appProyecto/padre.html')

def socios(req):
    return render(req, 'appProyecto/socios.html')

def profesores(req):
    return render(req, 'appProyecto/profesores.html')

def actividades(req):
    return render(req, 'appProyecto/actividades.html')

