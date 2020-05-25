from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator

# Create your models here.
class Clase(models.Model):
    # profesor = models.ForeignKey('Usuarios.Profesor', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    semestre = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(8)], blank=True, null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self):
        return "{} por {}".format(self.nombre, self.profesor)

    
class Parcial(models.Model):
    numero  = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)], blank=True, null=True)
    clase = models.ForeignKey('Clase', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Parcial'
        verbose_name_plural = 'Parciales'

    def __str__(self):
        return "Parcial {} de la clase {}".format(self.numero, self.clase)

class Unidad(models.Model):
    parcial = models.ForeignKey('Parcial', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    presentacion = models.CharField(max_length=1500)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return "{}".format(self.titulo)

    
