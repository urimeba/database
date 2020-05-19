from django.contrib import admin
from Apps.Ejercicios.models import Ejercicio, Intentos, Respuesta
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Ejercicio)
admin.site.register(Intentos)
admin.site.register(Respuesta)

