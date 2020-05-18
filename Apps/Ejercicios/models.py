from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator

# # Create your models here.
class tipoEjercicio(models.Model):
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    intentos = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(3)], blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo Ejercicio'
        verbose_name_plural = 'Tipos Ejercicios'

    def __str__(self):
        return "{} - Intentos: {}".format(self.descripcion, self.intentos)

class Ejercicio(models.Model):
    unidad = models.ForeignKey('Clases.Unidad', on_delete=models.CASCADE)
    tipo = models.ForeignKey('tipoEjercicio', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    archivo = models.FileField(upload_to='ejercicios/')
    is_active = models.BooleanField(default=False, blank=False, null=False)

    class Meta:
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'

    def __str__(self):
        return "Ejercicio #{} - Descripcion: {}".format(self.id, self.descripcion)

class Intentos(models.Model):
    alumno = models.ForeignKey('Usuarios.Alumno', on_delete=models.CASCADE)
    ejercicio = models.ForeignKey('Ejercicio', on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(default=3, null=False, blank=False,
        validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ])

    class Meta:
        verbose_name = 'Intento'
        verbose_name_plural = 'Intentos'



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
    alumno = models.ForeignKey('Usuarios.Alumno', on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

class CalificacionEjercicio(models.Model):
    ejercicio = models.ForeignKey('Ejercicio', on_delete=models.CASCADE)
    alumno = models.ForeignKey('Usuarios.Alumno', on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, default=0)