from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profesor, Alumno

admin.site.register(User, UserAdmin)
admin.site.register(Profesor)
admin.site.register(Alumno)
