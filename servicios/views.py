# servicios/views.py
from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.
# vista para la app de servicios
def servicios(request):
    servicios=Servicio.objects.all() #importe todos los servicios
    return render(request, "servicios/servicios.html", {"servicios":servicios})
