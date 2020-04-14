from django.contrib import admin
from Apps.Ejercicios.models import tipoEjercicio, Ejercicio, Intentos, Pregunta, OpcionRespuesta, Respuesta
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(tipoEjercicio)
admin.site.register(Ejercicio)
admin.site.register(Intentos)
admin.site.register(Pregunta)
admin.site.register(OpcionRespuesta)
admin.site.register(Respuesta)

