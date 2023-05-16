# tienda/urls.py
from django.urls import path

from . import views

# defincion de la url para la tienda
urlpatterns = [
    path('',views.tienda, name="Tienda"),

]
