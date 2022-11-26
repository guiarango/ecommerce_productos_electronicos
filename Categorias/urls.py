from django.contrib import admin
from django.urls import path
from Categorias.views import *

urlpatterns = [
    path('categorias/', categorias, name='categorias'),
]