from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

MAJORS = [
    ('SOF', 'Ingeniería de Software'),
    ('INF', 'Ingeniería en Informática'),
    ('LAT', 'Licenciatura en Administración de las TI'),
    ('INC', 'Ingeniería en Computación'),
    ('TEL', 'Ingeniería en Telecomunicaciones y Redes'),
]


class User(AbstractUser):
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    first_login = models.BooleanField(default=False, null=False, blank=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return "{}".format(self.username)

class Profesor(models.Model):
    usuario = models.OneToOneField('User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return "{}".format(self.usuario)

class Alumno(models.Model):
    usuario = models.OneToOneField('User', on_delete=models.CASCADE)
    clase = models.ForeignKey('Clases.Clase', on_delete=models.CASCADE)
    semestre = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    nacimiento = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    carrera = models.CharField(max_length=3, choices=MAJORS, blank=True, null=True)
    promedio = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        return "{}".format(self.usuario)



