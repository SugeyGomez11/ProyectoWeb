# servicios/urls.py
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

# Declaración de la url para la app de servicios
urlpatterns = [
    path('',views.servicios, name="Servicios"),
]

