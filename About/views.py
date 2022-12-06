from django.shortcuts import render,redirect
from About.forms import FundadoresFormulario
from About.models import Fundador
from datetime import datetime

# Create your views here.

def aboutPage(request):

    fundadores=Fundador.objects.all()
    contexto={"fundadores":fundadores}
    return render(request, 'About/about.html',contexto)


def crear_fundador(request):
    if request.method=="POST":
        formulario=FundadoresFormulario(request.POST,request.FILES)

        if formulario.is_valid():
            data=formulario.cleaned_data
            fundador=Fundador(nombre_completo=data["nombre_completo"], historia=data["historia"], imagen=data["imagen"],created=datetime.now())
            fundador.save()
            return redirect("about-listar-fundador")

    formulario=FundadoresFormulario()
    contexto={"formulario":formulario}
    return render(request, 'About/crear_fundador.html',contexto)

def listar_fundador(request):
    fundadores=Fundador.objects.all()
    contexto={"fundadores":fundadores}
    return render(request, 'About/listar_fundadores.html',contexto)


def editar_fundador(request,id):
    fundador=Fundador.objects.get(id=id)
    if request.method=="POST":
        formulario=FundadoresFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            data=formulario.cleaned_data
            fundador.nombre_completo=data["nombre_completo"]
            fundador.historia=data["historia"]
            fundador.imagen=data["imagen"]
            fundador.updated=datetime.now()
            fundador.save()
            return redirect("about-listar-fundador")

        else:
            return render(request,"About/editar_fundador.html",{"formulario":formulario,"errores":formulario.errors})
    else:
        formulario=FundadoresFormulario(initial={"nombre_completo":fundador.nombre_completo,"historia":fundador.historia,"imagen":fundador.imagen})
        return render(request,"About/editar_fundador.html",{"formulario":formulario,"errores":""})


def eliminar_fundador(request,id):
    fundador=Fundador.objects.get(id=id)
    fundador.delete()
    return redirect("about-listar-fundador")