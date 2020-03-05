from django.db import models
from Apps.Clases import models as models_clases
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator

# # Create your models here.

class Intentos(models.Model):
    alumno = models.ForeignKey(models_clases.Alumno, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey('Ejercicio', on_delete=models.CASCADE)

class Ejercicio(models.Model):
    unidad = models.ForeignKey(models_clases.Unidad, on_delete=models.CASCADE)
    tipo = models.ForeignKey('tipoEjercicio', on_delete=models.CASCADE)
    is_activated = models.BooleanField(default=False, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)

class tipoEjercicio(models.Model):
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    intentos = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(1)], blank=False, null=False)

class Pregunta(models.Model):
    ejercicio = models.ForeignKey('Ejercicio', on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=300, blank=False, null=True)

class OpcionRespuesta(models.Model):
    pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False, blank=False, null=True)

class Respuesta(models.Model):
    pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    alumno = models.ForeignKey(models_clases.Alumno, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=200, blank=True, null=True)