# blog/urls.py

# importación de las clases
from django.urls import path
from . import views

# Declaración de las urls para la app del blog
urlpatterns = [
    path('',views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
]