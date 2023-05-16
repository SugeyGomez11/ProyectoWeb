# carro/views.py

# Importación de las clases
from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.

# Funcion para agregar un producto
def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)

    return redirect("Tienda")

# Funcion para eliminar un producto
def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)

    return redirect("Tienda")

# Función para restar una cantidad de producto
def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_productos(producto=producto)

    return redirect("Tienda")

# Función para limpiar el carrito o productos
def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar_carro()

    return redirect("Tienda")