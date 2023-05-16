# carro/urls.py

# Importación de las clases
from django.urls import path

from . import views

# se especifica el nombre de la aplicación
app_name="carro"

# Declaración de las urls a utilizar
urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]
