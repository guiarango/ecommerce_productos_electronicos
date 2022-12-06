from django.contrib import admin
from Categorias.models import *

# Register your models here.

class TCategoriasAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

admin.site.register(TCategorias,TCategoriasAdmin)