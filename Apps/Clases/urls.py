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
from . import views as views_clases
from django.views.generic import TemplateView
from Apps.Clases import views as views_clases
from Apps.Ejercicios import views as views_ejercicios

urlpatterns = [
    path('', views_clases.Loginn.as_view(), name='Loginn'),
    path('dashboard', views_clases.dashboard, name='dashboard'),
    path('compilador', views_clases.compilador, name='compilador'),
    path('perfil', views_clases.perfil, name='perfil'),
    path('cerrarSesion', views_clases.cerrarSesion, name='cerrarSesion'),

    path('unidades', views_clases.unidades, name='unidades'),
    path('unidad/<int:pk>', views_clases.unidad, name='unidad'),
    path('unidad/<int:pk>/ejercicio/<int:id>', views_ejercicios.ejercicio, name='ejercicio'),
    
    
]
