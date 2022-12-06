from django.shortcuts import render
from Categorias.models import *

# Create your views here.

def categorias(request):
    categorias=CategoriaProd.objects.all()
    return render(request,'categorias/categorias.html', {"categorias":categorias})