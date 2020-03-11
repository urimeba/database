from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator

MAJORS = [
    ('SOF', 'Ingeniería de Software'),
    ('INF', 'Ingeniería en Informática'),
    ('LAT', 'Licenciatura en Administración de las TI'),
    ('INC', 'Ingeniería en Computación'),
    ('TEL', 'Ingeniería en Telecomunicaciones y Redes'),
]

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return str(self.username)

class Alumno(models.Model):
    usuario = models.OneToOneField('User', on_delete=models.CASCADE)
    clase = models.ForeignKey('Clase', on_delete=models.CASCADE)
    semestre = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    nacimiento = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    carrera = models.CharField(max_length=3, choices=MAJORS, blank=True, null=True)
    promedio = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'Alumnos'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        return str(self.usuario)

class Profesor(models.Model):
    usuario = models.OneToOneField('User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return str(self.usuario)

class Clase(models.Model):
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=200, blank=True, null=True)
    code_class = models.CharField(max_length=6, blank=True, null=True)
    semestre = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(8)], blank=True, null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self):
        return str(self.name) + " por " + str(self.profesor.usuario.username)

class ClaseParcial(models.Model):
    clase = models.ForeignKey('Clase', on_delete=models.CASCADE)
    parcial = models.ForeignKey('Parcial', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'ClaseParcial'
        verbose_name_plural = 'ClasesParciales'

    def __str__(self):
        return str(self.clase) + " - Parcial #" + str(self.parcial.numero)
    
class Parcial(models.Model):
    numero  = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)], blank=True, null=True)

    class Meta:
        verbose_name = 'Parcial'
        verbose_name_plural = 'Parciales'

    def __str__(self):
        return str(self.numero)

class Unidad(models.Model):
    parcial = models.ForeignKey('ClaseParcial', on_delete=models.CASCADE)
    presentation = models.FileField(upload_to='presentaciones/%Y/%m/%d/', max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return str(self.parcial) + " - Unidad#" + str(self.pk)

    
