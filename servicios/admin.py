# servicios/admin.py
from django.contrib import admin
from .models import Servicio

# Register your models here.
# Modelo para la administración de servicio
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)
