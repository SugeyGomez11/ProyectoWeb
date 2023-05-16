# blog/admin.py

#Importación de las clases
from django.contrib import admin
from .models import Categoria, Post

# Definicion de las clases para la categoria y las publicaciones
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
