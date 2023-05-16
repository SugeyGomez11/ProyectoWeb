# ProyectoWebApp/urls.py
from django.urls import path

from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

# Declaración de la url a utilizar en la aplicación de inicio
urlpatterns = [
    path('',views.home, name="Home"),

]

# Se carga en la carpeta media el contenido (imagenes)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)