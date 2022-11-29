from django.db import models

# Create your models here.
class Fundador(models.Model):
    nombre_completo=models.CharField(max_length=100)
    historia=models.TextField(max_length=500)
    imagen=models.ImageField(null=True, blank=True,upload_to="fundador/")
