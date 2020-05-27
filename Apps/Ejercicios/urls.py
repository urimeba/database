"""database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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


    path('respuestas31', views_ejercicios.respuestas31, name='respuestas31'),
    path('respuestas31/<int:idAlumno>', views_ejercicios.getRespuesta31, name='getRespuesta31'),
    path('calificaciones', views_ejercicios.getCalificaciones, name='getCalificaciones'),
    path('calificaciones/<int:idAlumno>', views_ejercicios.getCalificacionesAlumno, name='getCalificacionesAlumno'),
    path('setCalificacionAlumno', views_ejercicios.setCalificacionAlumno, name='setCalificacionAlumno'),
    path('ejercicios', views_ejercicios.ejercicios, name='ejercicios'),
    path('actualizarEjercicio', views_ejercicios.actualizarEjercicio, name='actualizarEjercicio'),
    
]
