from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import  send_mail
from pedidos.models import Pedido,LineaPedido
# Create your views here.
@login_required(login_url="/autenticacion/logear")

def procesar_pedido(request):
    pedido=Pedido.objetcs.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))
    LineaPedido.objetcs.bulk_create(lineas_pedidos)
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedidos,
        nombreusuario=request.user.username,
        emailusuario=request.user.email

    )

    messages.success(request, "el pedido se ha creado correctamente")
    return redirect ("../tienda")

def enviar_mail(**kwargs):

    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "linea_pedido": kwargs.get("linea_pedido"),
        "nombreusuario": kwargs.get("nombreusuario")

    })
    mensaje_texto=strip_tags(mensaje)
    from_email="barbargustavomili@gmail.com"
    #to=kwargs.get("emailusuario")
    to=barbara.lucia.pino@gmail.com
    send_mail(asunto,mensaje_texto,from_email,(to),html_message=mensaje)