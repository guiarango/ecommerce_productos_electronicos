from django.contrib import admin
from django.urls import path
from tienda.views import *

urlpatterns = [
    path('', tienda, name='tienda'),
]