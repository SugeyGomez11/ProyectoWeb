# carro/apps.py

# importacion de las clases
from django.apps import AppConfig

# Definición de la clase para la configuración de la app de carro
class CarroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carro'
