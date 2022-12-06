from django.contrib import admin
from django.urls import path
from pedidos.views import *




urlpatterns = [

    path('pedidos', procesar_pedido, name="procesar_predido"),

]
