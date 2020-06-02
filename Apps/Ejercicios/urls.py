from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from Apps.Ejercicios import views as views_ejercicios

urlpatterns = [
    path('<int:pk>', views_ejercicios.ejercicio, name='ejercicio'),
    path('setEjercicio11', views_ejercicios.ejercicio11, name='setEjercicio11'),
    path('setEjercicio21', views_ejercicios.ejercicio21, name='setEjercicio21'),
    path('setEjercicio22', views_ejercicios.ejercicio22, name='setEjercicio22'),
    path('setEjercicio23', views_ejercicios.ejercicio23, name='setEjercicio23'),
    path('setEjercicio31', views_ejercicios.ejercicio31, name='setEjercicio31'),
    path('setEjercicio51', views_ejercicios.ejercicio51, name='setEjercicio51'),
    path('setEjercicio71', views_ejercicios.ejercicio71, name='setEjercicio71'),


    path('dashboard', views_ejercicios.dashboard_profesor, name='dashboard_profesor'),
    path('respuestas31', views_ejercicios.respuestas31, name='respuestas31'),
    path('respuestas31/<int:idAlumno>', views_ejercicios.getRespuesta31, name='getRespuesta31'),
    path('calificaciones', views_ejercicios.getCalificaciones, name='getCalificaciones'),
    path('calificaciones/<int:idAlumno>', views_ejercicios.getCalificacionesAlumno, name='getCalificacionesAlumno'),
    path('setCalificacionAlumno', views_ejercicios.setCalificacionAlumno, name='setCalificacionAlumno'),
    path('ejercicios', views_ejercicios.ejercicios, name='ejercicios'),
    path('actualizarEjercicio', views_ejercicios.actualizarEjercicio, name='actualizarEjercicio'),
    
]
