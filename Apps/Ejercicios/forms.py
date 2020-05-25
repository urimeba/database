from django.forms import ModelForm
from .models import CalificacionEjercicio

class formEjercicio31(ModelForm):
    class Meta:
        model = CalificacionEjercicio
        fields = ['calificacion']
