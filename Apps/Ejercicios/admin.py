from django.contrib import admin
from Apps.Ejercicios import models as models_ejercicios
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(models_ejercicios.Intentos)
admin.site.register(models_ejercicios.Ejercicio)
admin.site.register(models_ejercicios.tipoEjercicio)
admin.site.register(models_ejercicios.Pregunta)
admin.site.register(models_ejercicios.Respuesta)
admin.site.register(models_ejercicios.OpcionRespuesta)
