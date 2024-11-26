from django.urls import path
from AppProyecto import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('socios/', views.socios, name='socios'),
    path('profesores/', views.profesores, name='profesores'),
    path('actividades/', views.actividades, name='actividades'),
    path('actividad-form/', views.actividad_form, name='actividad_form'),
    path('socio-form/', views.socio_form, name='socio_form'),



]