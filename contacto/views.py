from django.shortcuts import render , redirect
from contacto.forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto()
    
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if  formulario_contacto.is_valid():
              nombre=request.POST.get("Nombre")
              email=request.POST.get("Email")
              contenido=request.POST.get("Mensaje")
              email=EmailMessage("Mensaje desde App Django",
              "El usuario con nombre {} con la direccion {} te escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
              " ",["barbargustavomili@gmail.com "], reply_to=[email] )   
              try:
                   email.send ()   
                   
                   return redirect("/contacto/? valido")           
              except:
                 return redirect("/contacto/? valido")  
             
    return render(request,"contacto/contacto.html",{'miFormulario':formulario_contacto})