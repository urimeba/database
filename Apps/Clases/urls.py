from django.contrib import admin
from django.urls import path
from . import views as views_clases
from Apps.Clases import views as views_clases
from Apps.Ejercicios import views as views_ejercicios

urlpatterns = [
    path('', views_clases.Loginn.as_view(), name='Loginn'),
    path('dashboard', views_clases.dashboard, name='dashboard'),
    path('compilador', views_clases.compilador, name='compilador'),
    path('perfil', views_clases.perfil, name='perfil'),
    path('cerrarSesion', views_clases.cerrarSesion, name='cerrarSesion'),
    path('cambiarContraseña', views_clases.cambiarContraseña, name='cambiarContraseña'),

    path('unidades', views_clases.unidades, name='unidades'),
    path('unidad/<int:pk>', views_clases.unidad, name='unidad'),
    path('unidad/<int:pk>/ejercicio/<int:id>', views_ejercicios.ejercicio, name='ejercicio'),
    
    
]
