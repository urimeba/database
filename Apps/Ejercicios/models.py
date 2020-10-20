from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator

# Create your models here.
class Ejercicio(models.Model):
    unidad = models.ForeignKey('Clases.Unidad', on_delete=models.CASCADE)
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
    numero = models.PositiveIntegerField(default=2, null=False, blank=False,
        validators=[
            MaxValueValidator(2),
            MinValueValidator(0)
        ])

    class Meta:
        verbose_name = 'Intento'
        verbose_name_plural = 'Intentos'

    def __str__(self):
        return "{0} - Ejercicio: #{1}".format(self.alumno, self.ejercicio.id)

class Respuesta(models.Model):
    ejercicio = models.ForeignKey('Ejercicio', on_delete=models.CASCADE)
    alumno = models.ForeignKey('Usuarios.Alumno', on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

class CalificacionEjercicio(models.Model):
    alumno = models.ForeignKey('Usuarios.Alumno', on_delete=models.CASCADE)
    ejercicio = models.ForeignKey('Ejercicio', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, default=0,
    validators=[
            MaxValueValidator(10.00),
            MinValueValidator(0.00)
        ])