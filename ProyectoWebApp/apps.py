# ProyectoWebApp/apps.py
from django.apps import AppConfig

# Definicion de la clase para la configuracion de la aplicacion a nivel de proyecto general
class ProyectowebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProyectoWebApp'
