from django.contrib import admin
from django.urls import path
from About.views import *

urlpatterns = [
    path('', aboutPage, name='home'),
]