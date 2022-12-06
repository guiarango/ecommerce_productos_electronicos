from django.shortcuts import render,redirect
from Messages.forms import MessageForm
from django.core.mail import send_mail

# Create your views here.

def create_message_view(request):

    if request.method=="POST":
        formulario=MessageForm(request.POST)
        if formulario.is_valid():
            mensaje=formulario.cleaned_data
            send_mail(f'El usuario {mensaje.nombre_completo} ({mensaje.email}) te quiere contactar.',
            mensaje.mensaje,
            mensaje.email,
            ["barbargustavomili@gmail.com"])
            return redirect('message-sent')
        else:
            return render(request,"Messages/messageView.html",{"formulario":formulario,"errors":formulario.errors})
    else:
        formulario=MessageForm()
        return render(request,"Messages/messageView.html",{"formulario":formulario})


def message_sent(request):

    return render(request,"Messages/messageSent.html")