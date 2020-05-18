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
    
    # path('getEjercicio', views_ejercicios.getEjercicio, name='getEjercicio'),
    # path('setRespuestas', views_ejercicios.setRespuestas, name='setRespuestas'),
    path('setEjercicio11', views_ejercicios.ejercicio11, name='setEjercicio11'),
    path('setEjercicio21', views_ejercicios.ejercicio21, name='setEjercicio21'),
    path('setEjercicio22', views_ejercicios.ejercicio22, name='setEjercicio22'),
    path('setEjercicio23', views_ejercicios.ejercicio23, name='setEjercicio23'),
    
]
