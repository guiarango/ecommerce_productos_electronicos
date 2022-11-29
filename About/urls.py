from django.contrib import admin
from django.urls import path
from About.views import *

urlpatterns = [
    path('', aboutPage, name='about-landing'),
    path('crear_fundador/', crear_fundador, name='about-crear-fundador'),
    path('listar_fundador/', listar_fundador, name='about-listar-fundador'),
    path('editar_fundador/<id>', editar_fundador, name='about-editar-fundador'),
    path('eliminar_fundador/<id>', eliminar_fundador, name='about-eliminar-fundador'),
]

