# contacto/urls.py

# importación de las clases
from django.urls import path

from . import views

# declaración de la url a utilizar
urlpatterns = [
    path('',views.contacto, name="Contacto"),
]

