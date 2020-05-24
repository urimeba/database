# Generated by Django 2.2 on 2020-05-15 21:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clases', '0002_clase_profesor'),
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('archivo', models.FileField(upload_to='ejercicios/')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Ejercicio',
                'verbose_name_plural': 'Ejercicios',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=300, null=True)),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ejercicios.Ejercicio')),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Preguntas',
            },
        ),
        migrations.CreateModel(
            name='tipoEjercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('intentos', models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
            ],
            options={
                'verbose_name': 'Tipo Ejercicio',
                'verbose_name_plural': 'Tipos Ejercicios',
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(blank=True, max_length=200, null=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Alumno')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ejercicios.Pregunta')),
            ],
            options={
                'verbose_name': 'Respuesta',
                'verbose_name_plural': 'Respuestas',
            },
        ),
        migrations.CreateModel(
            name='OpcionRespuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False, null=True)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ejercicios.Pregunta')),
            ],
            options={
                'verbose_name': 'Opciones Respuesta',
                'verbose_name_plural': 'Opciones Respuestas',
            },
        ),
        migrations.CreateModel(
            name='Intentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Alumno')),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ejercicios.Ejercicio')),
            ],
            options={
                'verbose_name': 'Intento',
                'verbose_name_plural': 'Intentos',
            },
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ejercicios.tipoEjercicio'),
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clases.Unidad'),
        ),
    ]
