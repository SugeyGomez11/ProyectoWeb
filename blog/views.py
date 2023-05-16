# blog/views.py

# importación de las clases
from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

# Definicion de la vista para el blog
def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts":posts})

# Definicion de la vista para la categoria
def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias= categoria) #nos pueda filtrar por medio de la categoria
    return render(request, "blog/categoria.html", {'categoria': categoria, "posts":posts })

