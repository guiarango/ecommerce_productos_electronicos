from django.contrib import admin
from django.urls import path
from Messages.views import *

urlpatterns = [
    path('', create_message_view, name='message-landing'),
    path('message_sent/', message_sent, name='message-sent'),
]