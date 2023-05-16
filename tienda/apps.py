# tienda/apps.py
from django.apps import AppConfig

# Declaración de la clase para la configuracion de la aplicacion de la tienda
class TiendaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tienda'
