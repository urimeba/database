from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponse
from Apps.Usuarios.models import Alumno
from Apps.Clases.models import Unidad, Parcial
from Apps.Ejercicios.models import Ejercicio
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
import json
from .forms import formLogin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

class Loginn(LoginView):
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            form = formLogin()
            return render(request, 'login.html', {'form':form})
        return super().get(request, *args, **kwargs)

@login_required
def dashboard(request):
    if not request.user.first_login:
        return redirect('cambiarContraseña')

    return render(request, 'dashboard.html')

@login_required
def compilador(request):
    return render(request, 'compilador.html')

@login_required
def perfil(request):
    return render(request, 'profile.html')

@login_required
def unidades(request):
    alumno = Alumno.objects.get(usuario=request.user.id)
    parciales = Parcial.objects.filter(clase=alumno.clase)
    unidades = Unidad.objects.filter(parcial__in=parciales, is_active=True)

    if(alumno.clase.is_active):
        if(unidades.count() > 0):
            idUltimaUnidad = unidades.last().id
            return redirect('unidad', pk=idUltimaUnidad)
        else:
            return render(request, 'actividadesEjercicios.html')
    else:
        return redirect('dashboard')

@login_required
def unidad(request, pk):
    alumno = Alumno.objects.get(usuario=request.user.id)
    parciales = Parcial.objects.filter(clase=alumno.clase)
    unidades = Unidad.objects.filter(parcial__in=parciales)

    try:
        unidad_seleccionada = unidades.get(pk=pk)
    except:
        return redirect('dashboard')

    if(unidad_seleccionada.is_active):
        ejercicios = Ejercicio.objects.filter(unidad__id=unidad_seleccionada.id)
        return render(request, 'actividadesEjercicios.html', 
            {'unidades': unidades, 
            'ejercicios':ejercicios, 
            'unidad_seleccionada':unidad_seleccionada
            })
    else:
        return redirect('dashboard')

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

@login_required
def cambiarContraseña(request):
    form = PasswordChangeForm(user=request.user)

    first_login = False
    if not request.user.first_login:
        user = request.user
        user.first_login=True
        user.save()        
        first_login=True
        print("primera vez")

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST, )
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Important!
            messages.success(request, 'Contraseña cambiada correctamente')
            return render(request, 'cambiar_contraseña.html', {
                'form': form
            })
        else:
            return render(request, 'cambiar_contraseña.html', {
                'form': form
            })
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'cambiar_contraseña.html', {
            'form': form,
            'first_login': first_login
        })

