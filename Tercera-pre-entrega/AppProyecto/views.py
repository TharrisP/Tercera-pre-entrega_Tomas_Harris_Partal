from django.shortcuts import render
from .models import Actividades, Socios, Profesores
from AppProyecto.forms import ActividadFormulario, SocioFormulario, ProfesorFormulario

# Create your views here.

def inicio(req):
    return render(req, 'appProyecto/padre.html')

def socios(req):
    return render(req, 'appProyecto/socios.html')

def profesores(req):
    return render(req, 'appProyecto/profesores.html')

def actividades(req):
    return render(req, 'appProyecto/actividades.html')


def actividad_form(req):
    if req.method == "POST":

        miFormulario = ActividadFormulario(req.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data 
            actividad = Actividades(nombre=informacion["nombre"], valor=informacion["valor"]) 
            actividad.save() 
            return render(req, "AppProyecto/padre.html") 

    else:
        miFormulario = ActividadFormulario()

    return render(req, "AppProyecto/actividades.html", {"miFormulario": miFormulario})

def socio_form(req):
    if req.method == "POST":

        miFormulario = SocioFormulario(req.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data 
            socio = Socios(nombre=informacion["nombre"], apellido=informacion["apellido"],documento=informacion["documento"],email=informacion["email"],actividad=informacion["actividad"]) 
            socio.save()
            
            return render(req, "AppProyecto/padre.html") 

    else:
        miFormulario = SocioFormulario()

    return render(req, "AppProyecto/socios.html", {"miFormulario": miFormulario})

def profesor_form(req):
    if req.method == "POST":

        miFormulario = ProfesorFormulario(req.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data 
            profesor = Profesores(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],profesion=informacion["profesion"]) 
            profesor.save()
            
            return render(req, "AppProyecto/padre.html") 

    else:
        miFormulario = ProfesorFormulario()

    return render(req, "AppProyecto/profesores.html", {"miFormulario": miFormulario})



# def socio_buscar(req):
#     if req.GET('documento'):
#         docum = req.GET('documento')
