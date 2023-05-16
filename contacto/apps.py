# contacto/apps.py

# importación de la clase
from django.apps import AppConfig

# Declaración de la clase para la configuración de la app Contacto
class ContactoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contacto'
