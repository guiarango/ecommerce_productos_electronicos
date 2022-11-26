from django.contrib import admin
from django.urls import path
from Home.views import *

urlpatterns = [
    path('home/', home, name='home'),
]