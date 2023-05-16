# blog/apps.py
from django.apps import AppConfig

# declaracion de la clase para la configuracion del blog
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
