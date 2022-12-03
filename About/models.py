from django.db import models
from datetime import datetime

# Create your models here.
class Fundador(models.Model):
    nombre_completo=models.CharField(max_length=100)
    historia=models.TextField(max_length=500)
    imagen=models.ImageField(null=True, blank=True,upload_to="fundador/")
    created=models.DateTimeField(default=datetime.now())
    updated=models.DateTimeField(default=datetime.now())
# Soy un negociador internacional que encontró su pasión en la programación, tengo estudios como desarrollador web fullstack y QA manual. Actualmente soy desarrollador web para una empresa de ropa en Colombia.