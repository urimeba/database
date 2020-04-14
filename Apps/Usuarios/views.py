from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponse
from Apps.Usuarios.models import Alumno
from Apps.Clases.models import Unidad, Parcial
from Apps.Ejercicios.models import Ejercicio, Respuesta, Pregunta, Intentos
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
import json
from .forms import formLogin

# Create your views here.

# class Loginn(LoginView):
#     template_name = 'login.html'
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect(settings.LOGIN_REDIRECT_URL)
#         else:
#             form = formLogin()
#             return render(request, 'login.html', {'form':form})
#         return super().get(request, *args, **kwargs)