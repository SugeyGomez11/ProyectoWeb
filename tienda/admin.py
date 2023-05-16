# tienda/admin.py
from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.
# Modelo para la administración de los productos por categoria
class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

# Modelo para la administracion de los productos
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

# Se registra al sitio de administracion de django
admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)
