# tienda/views.py
from django.shortcuts import render
from .models import Producto

# Create your views here.
# Vista para la app de tienda
def tienda(request):
    productos=Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos":productos})