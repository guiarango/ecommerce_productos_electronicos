from django.db import models
from datetime import datetime

# Create your models here.

class Mensaje(models.Model):
    nombre_completo=models.CharField(max_length=100)
    email=models.EmailField()
    mensaje=models.CharField(max_length=500)