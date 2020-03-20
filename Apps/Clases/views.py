from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from Apps.Clases import forms as forms_clases
from Apps.Clases import models as models_clases
from Apps.Ejercicios import models as models_ejercicios
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json

class Loginn(LoginView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().get(request, *args, **kwargs)

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def compilator(request):
    return render(request, 'compilador.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def exercises(request):
    alumno = models_clases.Alumno.objects.get(usuario=request.user.id)
    clase = alumno.clase
    parciales = models_clases.ClaseParcial.objects.filter(clase=clase)
    temas = models_clases.Unidad.objects.filter(parcial__in=parciales)

    if(alumno.clase.is_active):
        if(temas.count()>0):
            ultima_unidad = temas.filter(is_active=True).last()
            ejercicios = models_ejercicios.Ejercicio.objects.filter(unidad=ultima_unidad)
            return render(request, 'actividadesEjercicios.html', {'temas': temas, 'ejercicios':ejercicios, 'ultima_unidad':ultima_unidad})
        else:
            return render(request, 'actividadesEjercicios.html')
    else:
        print("NO ES ACTIVA")


    return render(request, 'actividadesEjercicios.html')

@login_required
def changeUnity(request):
    idUnity = request.POST.get('idUnity')
    
    unity = models_clases.Unidad.objects.get(id=idUnity)
    data = {}
    data['title'] = unity.title
    data['description'] = unity.description
    data['presentation'] = unity.presentation
    return JsonResponse(data)

@login_required
def close(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)