# contacto/forms.py

# importación de las clases
from socket import fromshare
from django import forms 

# definicion de la clase para la creación del formulario para el contacto 
class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    email =  forms.CharField(label="Email", required=True)
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)
