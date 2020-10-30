from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from Apps.Ejercicios import views as views_ejercicios

urlpatterns = [
    path('<int:pk>', views_ejercicios.ejercicio, name='ejercicio'),
    path('setEjercicio01', views_ejercicios.ejercicio01, name='setEjercicio01'),
    path('setEjercicio11', views_ejercicios.ejercicio11, name='setEjercicio11'),
    path('setEjercicio21', views_ejercicios.ejercicio21, name='setEjercicio21'),
    path('setEjercicio22', views_ejercicios.ejercicio22, name='setEjercicio22'),
    path('setEjercicio23', views_ejercicios.ejercicio23, name='setEjercicio23'),
    path('setEjercicio31', views_ejercicios.ejercicio31, name='setEjercicio31'),
    path('setEjercicio32', views_ejercicios.ejercicio32, name='setEjercicio32'),
    path('setEjercicio41', views_ejercicios.ejercicio41, name='setEjercicio41'),
    path('setEjercicio42', views_ejercicios.ejercicio42, name='setEjercicio42'),
    path('setEjercicio51', views_ejercicios.ejercicio51, name='setEjercicio51'),
    path('setEjercicio52', views_ejercicios.ejercicio52, name='setEjercicio52'),
    path('setEjercicio61', views_ejercicios.ejercicio61, name='setEjercicio61'),
    path('setEjercicio62', views_ejercicios.ejercicio62, name='setEjercicio62'),
    path('setEjercicio71', views_ejercicios.ejercicio71, name='setEjercicio71'),
    path('setEjercicio72', views_ejercicios.ejercicio72, name='setEjercicio72'),
    path('setEjercicio81', views_ejercicios.ejercicio81, name='setEjercicio81'),
    path('setEjercicio82', views_ejercicios.ejercicio82, name='setEjercicio82'),
    path('setEjercicio91', views_ejercicios.ejercicio91, name='setEjercicio91'),


    path('dashboard', views_ejercicios.dashboard_profesor, name='dashboard_profesor'),
    path('respuestas31', views_ejercicios.respuestas31, name='respuestas31'),
    path('respuestas31/<int:idAlumno>', views_ejercicios.getRespuesta31, name='getRespuesta31'),
    path('calificaciones', views_ejercicios.getCalificaciones, name='getCalificaciones'),
    path('calificaciones/<int:idAlumno>', views_ejercicios.getCalificacionesAlumno, name='getCalificacionesAlumno'),
    path('setCalificacionAlumno', views_ejercicios.setCalificacionAlumno, name='setCalificacionAlumno'),
    path('ejercicios', views_ejercicios.ejercicios, name='ejercicios'),
    path('actualizarEjercicio', views_ejercicios.actualizarEjercicio, name='actualizarEjercicio'),
    path('addUser', views_ejercicios.addUser, name='addUser'),
]
