# ProyectoWebApp/views.py
from django.shortcuts import render, HttpResponse

# Create your views here.
# Vista para el inicio de la pagina
def home(request):
    return render(request, "ProyectoWebApp/home.html")



