from django.contrib import admin
from Apps.Clases import models as models_clases
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin )
admin.site.register(models_clases.Alumno)
admin.site.register(models_clases.Profesor)
admin.site.register(models_clases.Clase)
admin.site.register(models_clases.Parcial)
admin.site.register(models_clases.Unidad)
