from django.db import models

# Create your models here.
class TCategorias(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name ='Tcategorias'
        verbose_name_plural='Tcategorias'
        
    def __str__(self):
       return self.nombre
