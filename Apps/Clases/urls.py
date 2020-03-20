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

urlpatterns = [
    path('', views_clases.Loginn.as_view(), name='Loginn'),
    path('dashboard', views_clases.dashboard, name='dashboard'),
    path('compilator', views_clases.compilator, name='compilator'),
    path('profile', views_clases.profile, name='profile'),
    path('exercises', views_clases.exercises, name='exercises'),
    path('close', views_clases.close, name='close'),
    path('changeUnity', views_clases.changeUnity, name='changeUnity'),
]
