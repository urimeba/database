from django.db import models
from Apps.Clases import models as models_clases
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator

# # Create your models here.

class Intentos(models.Model):
    alumno = models.ForeignKey(models_clases.Alumno, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey('Ejercicio', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Intento'
        verbose_name_plural = 'Intentos'

class Ejercicio(models.Model):
    unidad = models.ForeignKey(models_clases.Unidad, on_delete=models.CASCADE)
    tipo = models.ForeignKey('tipoEjercicio', on_delete=models.CASCADE)
    is_activated = models.BooleanField(default=False, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'

    def __str__(self):
        return "Ejercicio #{} - Descripcion: {}".format(self.id, self.description)

class tipoEjercicio(models.Model):
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    intentos = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(3)], blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo Ejercicio'
        verbose_name_plural = 'Tipos Ejercicios'

    def __str__(self):
        return "{} - Intentos: {}".format(self.descripcion, self.intentos)

class Pregunta(models.Model):
    ejercicio = models.ForeignKey('Ejercicio', on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=300, blank=False, null=True)

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

class OpcionRespuesta(models.Model):
    pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False, blank=False, null=True)

    class Meta:
        verbose_name = 'Opciones Respuesta'
        verbose_name_plural = 'Opciones Respuestas'

class Respuesta(models.Model):
    pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    alumno = models.ForeignKey(models_clases.Alumno, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'