from import_export import resources
from import_export.fields import Field
from Apps.Usuarios.models import User, Profesor, Alumno 
from django.contrib.auth.hashers import make_password

class CategoriaResource(resources.ModelResource):
        
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','password')
        import_order = ('id','username','first_name','last_name','email','password')
class CategoriaResource2(resources.ModelResource):
    class Meta:
        model = Alumno
        fields = ('id','usuario','clase',)

        