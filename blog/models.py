# blog/models.py

# importación de las clases
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modelo para la categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

# Modelo para las publicaciones
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE) #si un usuario sale, se elimina su post
    categorias=models.ManyToManyField(Categoria) #tengan una relacion de muchos a muchos
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo
