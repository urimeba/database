from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profesor, Alumno
from import_export import resources 
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = User
        model = Alumno
        
class UsuarioAdmin(ImportExportModelAdmin,UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Extra', {
            'fields': (
                'is_maestro',
            )
        }),
    )
    resource_class = CategoriaResource

admin.site.register(User, UsuarioAdmin)
admin.site.register(Profesor)
admin.site.register(Alumno)
