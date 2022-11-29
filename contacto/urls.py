
from django.contrib import admin
from django.urls import path
from contacto.views import *


urlpatterns = [
      path('', contacto, name='contacto'),
]
