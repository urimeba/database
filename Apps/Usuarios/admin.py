from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profesor, Alumno
from import_export import resources 
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.hashers import make_password

class CategoriaResource(resources.ModelResource):
    def before_import_row(self,row, **kwargs):
        value = row['password']
        row['password'] = make_password(value)
    class Meta:
        model = User
        fields = ('id','password','username','first_name','last_name','email',)
        import_order = ('id','username','first_name','last_name','email','password')
        
class CategoriaResource2(resources.ModelResource):
    class Meta:
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

class UsuarioAlumno(ImportExportModelAdmin):
    class Meta:
        resource_class = CategoriaResource
      

admin.site.register(User, UsuarioAdmin)
admin.site.register(Profesor)
admin.site.register(Alumno, UsuarioAlumno)
