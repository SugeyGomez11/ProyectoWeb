# tienda/models.py
from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.
# Modelo para los productos por categoria
class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

    def __str__(self):
        return self.nombre
    
# Modelo para los productos de la tienda
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", null=True,blank=True) 
    precio=models.FloatField() 
    disponibilidad=models.BooleanField(default=True) 
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.nombre

    