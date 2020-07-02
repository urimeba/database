from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponse
from Apps.Usuarios.models import Alumno
from Apps.Clases.models import Unidad, Parcial
from Apps.Ejercicios.models import Ejercicio, CalificacionEjercicio
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
import json
from .forms import formLogin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import paramiko
from django.db.models import Avg

class Loginn(LoginView):
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_maestro:
                return redirect('dashboard_profesor')
            else:
                return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            form = formLogin()
            return render(request, 'login.html', {'form':form})
        return super().get(request, *args, **kwargs)

@login_required
def dashboard(request):
    if not request.user.first_login:
        return redirect('cambiarContraseña')

    if request.user.is_maestro:
        return redirect('dashboard_profesor')
    else:
        return render(request, 'dashboard.html')

@login_required
@csrf_exempt
def compilador(request):
    if(request.POST):
        ssh, stdout, stderr = ssh_send_query(request.session['_auth_user_id'], request.POST['query'])
        data = stdout.readlines()
        ssh_close(ssh)
        return JsonResponse({'data': data})
    else:
        return render(request, 'compilador.html')

def ssh_connect():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('132.145.55.249', username='opc', key_filename='./id_rsa.pub')
        return ssh
    except NameError:
        print("Ha ocurrido un error al conectar con el servidor SSH", NameError)


def ssh_close(ssh):
    try:
        ssh.close()
    except NameError:
        print("Ha ocurrido un error al cerrar conexión con el servidor SSH", NameError)

def ssh_send_query(user, query):
    try:
        ssh = ssh_connect()
        stdin, stdout, stderr = ssh.exec_command(
            'export TNS_ADMIN=/etc/ORACLE/WALLETS/ATP1 \n cd oracle-server \n node server {} "{}"'.format(user, query))
        return ssh, stdout, stderr
    except NameError:
        print("Ha ocurrido un error al enviar la petición al servidor SSH", NameError)


@login_required
def perfil(request):
    alumno = Alumno.objects.get(usuario=request.user)
    calificaciones = CalificacionEjercicio.objects.filter(
        alumno = alumno
    ).order_by('ejercicio__unidad')

    validas = calificaciones.filter(calificacion__gt=0)
    promedio = validas.aggregate(Avg('calificacion'))

        
    datos = []
    for calificacion in validas:
        idUnidad = "Unidad " + str(calificacion.ejercicio.unidad.id)
        
        lenDatos = len(datos)
        cont = 0
        for obj in datos:
            if(obj["mapname"]!=idUnidad):
                cont+=1
        
        if(lenDatos==cont):
            datos.append({"mapname":idUnidad})

        
        for obj in datos:
            ind = datos.index(obj)
            idUni = obj["mapname"]
            if(idUni==idUnidad):
                index = ind

        jsonData = datos[index]
        lent = len(jsonData)
        if(lent==1):
            jsonData["value"] = str(calificacion.calificacion)
        else:
            strValue = "value" + str(lent)
            jsonData[strValue] = str(calificacion.calificacion)
            



    return render(request, 'profile.html', {
        'calificaciones':calificaciones,
        'promedio':promedio,
        'datos':datos
    })

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

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST, )
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Contraseña cambiada correctamente')
            ssh_send_query(request.session['_auth_user_id'], 'pwrird7qWf')
            return render(request, 'dashboard.html', {
                'form': form
            })
        else:
            return render(request, 'cambiar_contrasena.html', {
                'form': form
            })
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'cambiar_contrasena.html', {
            'form': form,
            'first_login': first_login
        })

