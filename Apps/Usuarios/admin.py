from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profesor, Alumno

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Extra', {
            'fields': (
                'is_maestro',
            )
        }),
    )

admin.site.register(User, UsuarioAdmin)
admin.site.register(Profesor)
admin.site.register(Alumno)
