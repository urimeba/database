from import_export import resources  
from Apps.Usuarios.models import User, Profesor, Alumno 


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id','password','username','first_name','last_name','email',)

class CategoriaResource2(resources.ModelResource):
    class Meta:
        model = Alumno
        fields = ('id','usuario','clase','semestre','nacimiento','carrera','promedio',)