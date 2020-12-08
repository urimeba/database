from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from Apps.Clases.models import Unidad, Parcial, Clase
from Apps.Usuarios.models import Alumno, Profesor, User
from Apps.Ejercicios.models import Ejercicio, Respuesta, Intentos, CalificacionEjercicio
from .forms import formEjercicio31
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import tablib
from django.contrib import messages
from decimal import Decimal
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import localtime, now
from tablib import Dataset 
from Apps.Usuarios.admin import CategoriaResource, CategoriaResource2
# Create your views here.
@login_required
def ejercicio(request, pk, id):
    alumno = Alumno.objects.get(usuario=request.user.id)
    parciales = Parcial.objects.filter(clase=alumno.clase)
    unidades = Unidad.objects.filter(parcial__in=parciales)
    ejercicios = Ejercicio.objects.filter(unidad__id=pk)
    respuesta = None

    try:
        unidad = Unidad.objects.get(pk=pk)
    except Exception as error:
        print(error)
        return redirect('dashboard')

    try:
        ejercicio = Ejercicio.objects.get(id=id, unidad=unidad)
        alumno = Alumno.objects.get(usuario__id=request.user.id)
        numeroIntentos, createdIntentos = Intentos.objects.get_or_create(
            ejercicio=ejercicio, 
            alumno=alumno)

        calificacion, createdCalificacion = CalificacionEjercicio.objects.get_or_create(
            ejercicio = ejercicio, 
            alumno = alumno
            )

        respuesta = Respuesta.objects.filter(
            ejercicio=ejercicio,
            alumno=alumno
        )
    except Exception as error:
        print(error)
        return redirect('dashboard')

    
    return render(request, str(ejercicio.archivo),{
        'ejercicio_seleccionado':ejercicio,
        'unidades': unidades, 
        'ejercicios':ejercicios,
        'intentos': str(numeroIntentos.numero),
        'respuestas':respuesta,
        'calificacion':calificacion
    })

@login_required
def ejercicio01(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=1, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 1,
        alumno = alumno
        )

    if(intentos.numero>0):
        # Creando un nuevo intento
        fechaActual = datetime.now()
        intentos.numero-=1
        intentos.save()

        calificacion = 0

        res1 = request.POST['res1']
        res2 = request.POST['res2']
        res3 = request.POST['res3']
        res4 = request.POST['res4']
        res5 = request.POST['res5']
        res6 = request.POST['res6']
        res7 = request.POST['res7']
        res8 = request.POST['res8']
        res9 = request.POST['res9']
        res10 = request.POST['res10']

        if (res1 == "c"):
            calificacion+=1

        if (res2 == "a"):
            calificacion += 1

        if (res3 == "b"):
            calificacion += 1

        if (res4 == "c"):
            calificacion += 1

        if (res5 == "b"):
            calificacion += 1

        if (res6 == "a"):
            calificacion += 1

        if (res7 == "b"):
            calificacion += 1

        if (res8 == "a"):
            calificacion += 1

        if (res9 == "a"):
            calificacion += 1

        if (res10 == "c"):
            calificacion += 1

    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Repositorio de información digital \n 2.-Modelo de organización de bases de datos \n 3.-Comandos para la busqueda de información especifica \n 4.-Representación de un registro \n 5.-Representacion de un atributo \n 6.-Representación minima de un atributo \n 7.-Sistema de manipulación y mantenimiento de datos \n 8.-Definición de propiedades a cumplir por la información a ingresar \n 9.-Manera en la cual se relacionan las tablas \n 10.-Representación grafica de una base de datos",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Repositorio de información digital \n 2.-Modelo de organización de bases de datos \n 3.-Comandos para la busqueda de información especifica \n 4.-Representación de un registro \n 5.-Representacion de un atributo \n 6.-Representación minima de un atributo \n 7.-Sistema de manipulación y mantenimiento de datos \n 8.-Definición de propiedades a cumplir por la información a ingresar \n 9.-Manera en la cual se relacionan las tablas \n 10.-Representación grafica de una base de datos",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })
        

# ID DEL EJERCICIO: 6
@login_required
def ejercicio11(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=2, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 2,
        alumno = alumno
        )


    if(intentos.numero>0):
        # Creando un nuevo intento
        fechaActual = datetime.now()
        intentos.numero-=1
        intentos.save()

        calificacion = 0

        res1 = request.POST['res1']
        res2 = request.POST['res2']
        res3 = request.POST['res3']
        res4 = request.POST['res4']
        res5 = request.POST['res5']
        res6 = request.POST['res6']
        res7 = request.POST['res7']
        res8 = request.POST['res8']
        res9 = request.POST['res9']
        res10 = request.POST['res10']

        if (res1 == "c"):
            calificacion+=1

        if (res2 == "b"):
            calificacion += 1

        if (res3 == "a"):
            calificacion += 1

        if (res4 == "a"):
            calificacion += 1

        if (res5 == "b"):
            calificacion += 1

        if (res6 == "c"):
            calificacion += 1

        if (res7 == "b"):
            calificacion += 1

        if (res8 == "a"):
            calificacion += 1

        if (res9 == "a"):
            calificacion += 1

        if (res10 == "b"):
            calificacion += 1

    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Datos \n 2.-Bases de datos \n 3.-datos relacionados \n 4.-Colección integrada \n 5.-Conjuntos de programas de administración de BD \n 6.-Un gerente de proyectos \n 7.-Llevar la información a su minima expresión \n 8.-Procesos del sistema operativo \n 9.-Restricciones y consistencia \n 10.-Minimizar redundancia",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Datos \n 2.-Bases de datos \n 3.-datos relacionados \n 4.-Colección integrada \n 5.-Conjuntos de programas de administración de BD \n 6.-Un gerente de proyectos \n 7.-Llevar la información a su minima expresión \n 8.-Procesos del sistema operativo \n 9.-Restricciones y consistencia \n 10.-Minimizar redundancia",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })
# ID DEL EJERCICIO: 3
@login_required
def ejercicio21(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=3, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 3,
        alumno = alumno
        )

    if(intentos.numero>0):
        intentos.numero-=1
        intentos.save()

        calificacion = 0
        atributosVideojuegos = json.loads(request.POST['atributosVideojuegos'])
        atributosProveedores = json.loads(request.POST['atributosProveedores'])
        atributosEmpleados = json.loads(request.POST['atributosEmpleados'])
        atributosClientes = json.loads(request.POST['atributosClientes'])

        calificacion+=0.589 if 'Titulo' in atributosVideojuegos else 0
        calificacion+=0.589 if 'Genero' in atributosVideojuegos else 0
        calificacion+=0.589 if 'Consola' in atributosVideojuegos else 0
        calificacion+=0.589 if 'Desarrollador' in atributosVideojuegos else 0
        calificacion+=0.589 if 'Precio' in atributosVideojuegos else 0
        calificacion+=0.589 if 'Fecha de lanzamiento' in atributosVideojuegos else 0

        calificacion+=0.589 if 'Nombre' in atributosProveedores else 0
        calificacion+=0.589 if 'Telefono' in atributosProveedores else 0
        calificacion+=0.589 if 'Direccion' in atributosProveedores else 0
        calificacion+=0.589 if 'Clave' in atributosProveedores else 0

        calificacion+=0.589 if 'Nombre' in atributosEmpleados else 0
        calificacion+=0.589 if 'Sucursal' in atributosEmpleados else 0
        calificacion+=0.589 if 'Salario' in atributosEmpleados else 0

        calificacion+=0.589 if 'Nombre' in atributosClientes else 0
        calificacion+=0.589 if 'Direccion' in atributosClientes else 0
        calificacion+=0.589 if 'Correo electronico' in atributosClientes else 0
        calificacion+=0.589 if 'Telefono' in atributosClientes else 0


        calificacion=10 if calificacion>10 else round(calificacion, 2)
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n \n Videojuegos: \n -Titulo \n -Genero \n -Consola \n -Desarrollador \n -Precio \n -Fecha de lanzamiento \n \n Proveedores: \n -Nombre \n -Telefono \n -Dirrección \n -Clave \n \n Empleados \n -Nombre \n -Sucursal \n -Salario \n \n Clientes: \n -Nombre \n -Dirección \n -Correo Electronico \n -Telefono",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        if(intentos.numero == 0):
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n \n Videojuegos: \n -Titulo \n -Genero \n -Consola \n -Desarrollador \n -Precio \n -Fecha de lanzamiento \n \n Proveedores: \n -Nombre \n -Telefono \n -Dirrección \n -Clave \n \n Empleados \n -Nombre \n -Sucursal \n -Salario \n \n Clientes: \n -Nombre \n -Dirección \n -Correo Electronico \n -Telefono",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
                })
        else:
            return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion       
            })
# ID DEL EJERCICIO: 7
@login_required
def ejercicio22(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=4, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
            ejercicio_id = 4,
            alumno = alumno
        )

    if(intentos.numero>0):
        intentos.numero-=1
        intentos.save()

        calificacion = 0
        atributosOracle = json.loads(request.POST['atributosOracle'])
        atributosmysql = json.loads(request.POST['atributosmysql'])
        atributospostgres = json.loads(request.POST['atributospostgres'])

        calificacion+=0.556 if 'varchar2' in atributosOracle else 0
        calificacion+=0.556 if 'rowid' in atributosOracle else 0
        calificacion+=0.556 if 'raw' in atributosOracle else 0
        calificacion+=0.556 if 'nchar' in atributosOracle else 0
        calificacion+=0.556 if 'binary_double' in atributosOracle else 0
        calificacion+=0.556 if 'number' in atributosOracle else 0

        calificacion+=0.556 if 'mediumint' in atributosmysql else 0
        calificacion+=0.556 if 'year' in atributosmysql else 0
        calificacion+=0.556 if 'varchar' in atributosmysql else 0
        calificacion+=0.556 if 'text' in atributosmysql else 0
        calificacion+=0.556 if 'time' in atributosmysql else 0
        calificacion+=0.556 if 'bigint' in atributosmysql else 0

        calificacion+=0.556 if 'serial' in atributospostgres else 0
        calificacion+=0.556 if 'box' in atributospostgres else 0
        calificacion+=0.556 if 'character' in atributospostgres else 0
        calificacion+=0.556 if 'double precision' in atributospostgres else 0
        calificacion+=0.556 if 'line' in atributospostgres else 0
        calificacion+=0.556 if 'money' in atributospostgres else 0

        calificacion=10 if calificacion>10 else round(calificacion, 2)
        
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n \n Oracle: \n -varchar2 \n -rowid \n -raw \n -nchar \n -binary_double \n -number \n \n MySQL: \n -mediumint \n -year \n -varchar \n -text \n -time \n -bigint \n \n Postgres: \n -serial \n -box \n -character \n -double precision \n -line \n -money",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        if(intentos.numero == 0):
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n \n Oracle: \n -varchar2 \n -rowid \n -raw \n -nchar \n -binary_double \n -number \n \n MySQL: \n -mediumint \n -year \n -varchar \n -text \n -time \n -bigint \n \n Postgres: \n -serial \n -box \n -character \n -double precision \n -line \n -money",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
                })
        else:
            return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion       
            })
# ID DEL EJERCICIO: 8
@login_required
def ejercicio23(request):

    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=5, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 5,
        alumno = alumno
        )

    if(intentos.numero>0):
        intentos.numero-=1
        intentos.save()

        calificacion = 0
        atributosCaracter = json.loads(request.POST['atributosCaracter'])
        atributosNumericos = json.loads(request.POST['atributosNumericos'])
        atributosFecha = json.loads(request.POST['atributosFecha'])
        atributosObjetos = json.loads(request.POST['atributosObjetos'])

        calificacion+=0.527 if 'varchar2' in atributosCaracter else 0
        calificacion+=0.527 if 'nchar' in atributosCaracter else 0
        calificacion+=0.527 if 'char' in atributosCaracter else 0
        calificacion+=0.527 if 'long raw' in atributosCaracter else 0
        calificacion+=0.527 if 'raw' in atributosCaracter else 0
        calificacion+=0.527 if 'long' in atributosCaracter else 0
        calificacion+=0.527 if 'nvarchar2' in atributosCaracter else 0

        calificacion+=0.527 if 'binary float' in atributosNumericos else 0
        calificacion+=0.527 if 'binary double' in atributosNumericos else 0
        calificacion+=0.527 if 'number' in atributosNumericos else 0

        calificacion+=0.527 if 'date' in atributosFecha else 0
        calificacion+=0.527 if 'interval' in atributosFecha else 0
        calificacion+=0.527 if 'timestamp with local zone' in atributosFecha else 0
        calificacion+=0.527 if 'timestamp with local time zone' in atributosFecha else 0
        calificacion+=0.527 if 'timestamp' in atributosFecha else 0

        calificacion+=0.527 if 'bfile' in atributosObjetos else 0
        calificacion+=0.527 if 'nclob' in atributosObjetos else 0
        calificacion+=0.527 if 'clob' in atributosObjetos else 0
        calificacion+=0.527 if 'blob' in atributosObjetos else 0

        calificacion=10 if calificacion>10 else round(calificacion, 2)
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n \n Caracter: \n -varchar2 \n -nchar \n -char \n -long raw \n -raw \n -long \n -nvarchar 2 \n \n Numericos: \n -binary float \n -binary double \n -number \n \n Fecha: \n -date \n -interval \n -timestamp with local zone \n -timestamp with local time zone \n -timestamp \n \n Objetos \n -bfile \n -nclob \n -clob \n -blob",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        if(intentos.numero == 0):
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n \n Caracter: \n -varchar2 \n -nchar \n -char \n -long raw \n -raw \n -long \n -nvarchar 2 \n \n Numericos: \n -binary float \n -binary double \n -number \n \n Fecha: \n -date \n -interval \n -timestamp with local zone \n -timestamp with local time zone \n -timestamp \n \n Objetos: \n -bfile \n -nclob \n -clob \n -blob",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
                })
        else:
            return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion       
            })
# ID DEL EJERCICIO: 2
# EJERCICIO DE LA TABLA
@login_required
def ejercicio31(request):

    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=6, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 6,
        alumno = alumno
        )

    if(intentos.numero>0):
        tabla = request.POST['tabla']
        print(tabla)

        intentos.numero-=1
        intentos.save()
        
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()


        respuesta, created = Respuesta.objects.get_or_create(
            ejercicio_id = 6,
            alumno = alumno
        )
        respuesta.respuesta=tabla
        respuesta.save()


        return JsonResponse({
            'calificacion': "Tu calificacion sera evaluada por tu profesor. (Intentos restantes: {0} intento(s))"
            .format(intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

@login_required
def ejercicio32(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=7, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 7,
        alumno = alumno
        )


    if(intentos.numero>0):
        # Creando un nuevo intento
        fechaActual = datetime.now()
        intentos.numero-=1
        intentos.save()

        calificacion = 0

        res1 = request.POST['res1']
        res2 = request.POST['res2']
        res3 = request.POST['res3']
        res4 = request.POST['res4']
        res5 = request.POST['res5']
        res6 = request.POST['res6']
        res7 = request.POST['res7']
        res8 = request.POST['res8']
        res9 = request.POST['res9']
        res10 = request.POST['res10']

        if (res1 == "a"):
            calificacion+=1

        if (res2 == "b"):
            calificacion += 1

        if (res3 == "a"):
            calificacion += 1

        if (res4 == "b"):
            calificacion += 1

        if (res5 == "c"):
            calificacion += 1

        if (res6 == "b"):
            calificacion += 1

        if (res7 == "b"):
            calificacion += 1

        if (res8 == "a"):
            calificacion += 1

        if (res9 == "d"):
            calificacion += 1

        if (res10 == "d"):
            calificacion += 1
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Sistema manejador de bases de datos \n 2.-cuando no es necesario el acceso concurrente \n 3.-Data definition language \n 4.-Data manipulation language \n 5.-Delete \n 6.-Drop \n 7.-Representación simple de las tablas y las relaciónes \n 8.-Estructura donde se almacena la información \n 9.-Todas las anteriores \n 10.-Todas las anteriores",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Sistema manejador de bases de datos \n 2.-cuando no es necesario el acceso concurrente \n 3.-Data definition language \n 4.-Data manipulation language \n 5.-Delete \n 6.-Drop \n 7.-Representación simple de las tablas y las relaciónes \n 8.-Estructura donde se almacena la información \n 9.-Todas las anteriores \n 10.-Todas las anteriores",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })
@login_required
def ejercicio41(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=8, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 8,
        alumno = alumno
        )

    if(intentos.numero>0):
        # Creando un nuevo intento
        fechaActual = datetime.now()
        intentos.numero-=1
        intentos.save()

        calificacion = 0

        res1 = request.POST['res1']
        res2 = request.POST['res2']
        res3 = request.POST['res3']
        res4 = request.POST['res4']
        res5 = request.POST['res5']
        res6 = request.POST['res6']
        res7 = request.POST['res7']
        res8 = request.POST['res8']
        res9 = request.POST['res9']
        res10 = request.POST['res10']

        if (res1 == "b"):
            calificacion+=1

        if (res2 == "c"):
            calificacion += 1

        if (res3 == "a"):
            calificacion += 1

        if (res4 == "a"):
            calificacion += 1

        if (res5 == "e"):
            calificacion += 1

        if (res6 == "a"):
            calificacion += 1

        if (res7 == "b"):
            calificacion += 1

        if (res8 == "e"):
            calificacion += 1

        if (res9 == "c"):
            calificacion += 1

        if (res10 == "b"):
            calificacion += 1
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Reconocer filas iguales \n 2.-Dato unico e irrepetible para buscar y comparar registros \n 3.-Varias tablas que necesitan reglas de integridad \n 4.-Estructurales y semanticas \n 5.-Todas las anteriores \n 6.-Relaciones entre filas de una tabla con las filas de otra tabla \n 7.-Llave foranea y llave primaria \n 8.-Todas las anteriores \n 9.-Aplicación \n 10.-Modelo",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Reconocer filas iguales \n 2.-Dato unico e irrepetible para buscar y comparar registros \n 3.-Varias tablas que necesitan reglas de integridad \n 4.-Estructurales y semanticas \n 5.-Todas las anteriores \n 6.-Relaciones entre filas de una tabla con las filas de otra tabla \n 7.-Llave foranea y llave primaria \n 8.-Todas las anteriores \n 9.-Aplicación \n 10.-Modelo",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })
@login_required
def ejercicio42(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=9, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 9,
        alumno = alumno
        )

    if(intentos.numero>0):
        intentos.numero-=1
        intentos.save()

        calificacion = 0
        atributosPrestamo = json.loads(request.POST['atributosPrestamo'])
        tamañoAtributos = len(atributosPrestamo)
        calificacionNegativa=(6-tamañoAtributos)*(0.5) if tamañoAtributos>6 else 0
        print(calificacionNegativa)

        calificacion+=1.67 if 'PK - ID(number)' in atributosPrestamo else 0
        calificacion+=1.67 if 'FK - expedienteAlumno(number)' in atributosPrestamo else 0
        calificacion+=1.67 if 'FK - isbn(number)' in atributosPrestamo else 0
        calificacion+=1.67 if 'FK - claveEmpleado(number)' in atributosPrestamo else 0
        calificacion+=1.67 if 'fechaPrestamo(date)' in atributosPrestamo else 0
        calificacion+=1.67 if 'fechaEntrega(date)' in atributosPrestamo else 0

        calificacion = calificacion + calificacionNegativa
        calificacion=10 if calificacion>10 else round(calificacion, 2)
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos)",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        if(intentos.numero == 0):
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos)",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
                })
        else:
            return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion       
            })
# NECESARIO EL SERVIDOR SQL DE ORACLE
@login_required
def ejercicio51(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=10, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 10,
        alumno = alumno
        )

    if(intentos.numero>0):
        query = request.POST['query']
        calificacion = 0
        querys = query.lower().split(';')
        
        for queri in querys:
            queri = queri.replace(" ", "")
            attrs = queri.split(",")
            print(attrs)

            if("createtablelibros" in attrs[0]):
                for attr in attrs:
                    if("isbnnumber(13)primarykey" in attr):
                        calificacion+=0.44
                    if("titulovarchar2(100)notnull" in attr):
                        calificacion+=0.44
                    if("ubicacionvarchar2(100)notnull" in attr):
                        calificacion+=0.44
                    if("autorvarchar2(100)notnull" in attr):
                        calificacion+=0.44
                    if("editorialvarchar2(100)notnull" in attr):
                        calificacion+=0.44
            
            if("createtableempleados" in attrs[0]):
                for attr in attrs:
                    if("clavenumber(7)primarykey" in attr):
                        calificacion+=0.44
                    if("nombreempleadovarchar2(100)notnull" in attr):
                        calificacion+=0.44
                    if("puestovarchar2(100)notnull" in attr):
                        calificacion+=0.44
                    if("fechacontrataciondatenotnull" in attr):
                        calificacion+=0.44
                    if("constraintempleados_uniqueunique(puesto)" in attr):
                        calificacion+=0.44

            if("createtablealumnos" in attrs[0]):
                for attr in attrs:
                    if("expedientenumber(6)primarykey" in attr):
                        calificacion+=0.44
                    if("nombrealumnovarchar2(100)notnull" in attr):
                        calificacion+=0.44
                    if("planvarchar2(100)notnull" in attr):
                        calificacion+=0.44
                    if("fechaingresodatenotnull" in attr):
                        calificacion+=0.44

            if("createtableprestamo" in attrs[0]):
                for attr in attrs:
                    if("idnumber(7)primarykey" in attr):
                        calificacion+=0.44
                    if("isbnnumber(13)notnull" in attr):
                        calificacion+=0.44
                    if("claveempleadonumber(7)notnull" in attr):
                        calificacion+=0.44
                    if("expedientealumnonumber(6)notnull" in attr):
                        calificacion+=0.44
                    if("fechaprestamodatenotnull" in attr):
                        calificacion+=0.44
                    if("fechaentregadatenotnull" in attr):
                        calificacion+=0.44
                    if("constraintfk_isbnforeignkey(isbn)referenceslibros(isbn)" in attr):
                        calificacion+=0.44
                    if("constraintfk_claveempleadoforeignkey(claveempleado)referencesempleados(clave)" in attr):
                        calificacion+=0.44
                    if("constraintfk_expedientealumnoforeignkey(expedientealumno)referencesalumnos(expediente)" in attr):
                        calificacion+=0.44


        intentos.numero-=1
        intentos.save()
        
        calificacion=10 if calificacion>10 else round(calificacion, 2)
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        respuesta, created = Respuesta.objects.get_or_create(
            ejercicio_id = 10,
            alumno = alumno
        )
        respuesta.respuesta=query
        respuesta.save()


        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })
    if(intentos.numero == 0):
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

@login_required
def ejercicio52(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=11, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 11,
        alumno = alumno
        )

    if(intentos.numero>0):
        intentos.numero-=1
        intentos.save()

        calificacion = 0
        atributosNotNull = json.loads(request.POST['atributosNotNull'])
        atributosUnique = json.loads(request.POST['atributosUnique'])
        atributosPrimaryKey = json.loads(request.POST['atributosPrimaryKey'])
        atributosForeignKey = json.loads(request.POST['atributosForeignKey'])
        atributosCheck = json.loads(request.POST['atributosCheck'])
        atributosDefault = json.loads(request.POST['atributosDefault'])

        calificacion+=0.77 if 'Habilita la posibilidad de ingresar valores nulos' in atributosNotNull else 0

        calificacion+=0.77 if 'Habilita la imposibilidad de ingresar dos valores iguales en la misma columna' in atributosUnique else 0
        calificacion+=0.77 if 'Es posible ingresar valores nulos' in atributosUnique else 0

        calificacion+=0.77 if 'Solo puede existir una por tabla' in atributosPrimaryKey else 0
        calificacion+=0.77 if 'NO puede contener valores nulos' in atributosPrimaryKey else 0
        calificacion+=0.77 if 'NO pueden existir dos valores en esta columna' in atributosPrimaryKey else 0

        calificacion+=0.77 if 'Restingue los valores de una columna con base en los valores de otra tabla' in atributosForeignKey else 0
        calificacion+=0.77 if 'SI puede contener valores nulos' in atributosForeignKey else 0
        calificacion+=0.77 if 'Es posible que sea autoreferencial' in atributosForeignKey else 0

        calificacion+=0.77 if 'Habilita la posibilidad de realizar validacion a los datos antes de ingresarlos a la BD' in atributosCheck else 0
        calificacion+=0.77 if 'Usada para definir valores predeterminados o revisar que esten dentro de un rango de numeros' in atributosCheck else 0

        calificacion+=0.77 if 'Establece un valor predeterminado si no se especifica uno' in atributosDefault else 0
        calificacion+=0.77 if 'Reduce la carga de trabajo para la persona que llena formularios' in atributosDefault else 0

        calificacion=10 if calificacion>10 else round(calificacion, 2)
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n \n NULL/NOT NULL: \n -Habilita la posibilidad de ingresar valores nulos \n \n UNIQUE \n -Habilita la imposibilidad de ingresar dos valores iguales en la misma columna \n -Es posible ingresar valores nulos \n \n PRIMARY KEY: \n -Solo puede existir una por tabla \n -NO puede contener valores nulos \n -NO pueden existir dos valores en esta columna \n \n FOREGIN KEY: \n -Restringe los valores de una columna con base en los valores de otra tabla \n -SI puede contener valores nulos \n -Es posible que sea autoreferencial \n \n CHECK: \n -Usada para definir valores predeterminados o revisar que esten dentro de un rango de numeros \n -Habilita la posibilidad de realizar validacion a los datos antes de ingresarlos a al BD \n \n DEFAULT \n -Establece un valor predeterminado si no se especifica uno \n -Reduce la carga de trabajo para la persona que llena formularios",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        if(intentos.numero == 0):
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n \n NULL/NOT NULL: \n -Habilita la posibilidad de ingresar valores nulos \n \n UNIQUE \n -Habilita la imposibilidad de ingresar dos valores iguales en la misma columna \n -Es posible ingresar valores nulos \n \n PRIMARY KEY: \n -Solo puede existir una por tabla \n -NO puede contener valores nulos \n -NO pueden existir dos valores en esta columna \n \n FOREGIN KEY: \n -Restringe los valores de una columna con base en los valores de otra tabla \n -SI puede contener valores nulos \n -Es posible que sea autoreferencial \n \n CHECK: \n -Usada para definir valores predeterminados o revisar que esten dentro de un rango de numeros \n -Habilita la posibilidad de realizar validacion a los datos antes de ingresarlos a al BD \n \n DEFAULT \n -Establece un valor predeterminado si no se especifica uno \n -Reduce la carga de trabajo para la persona que llena formularios",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
                })
        else:
            return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion       
            })
@login_required
def ejercicio61(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=12, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 12,
        alumno = alumno
        )

    if(intentos.numero>0):
        # Creando un nuevo intento
        fechaActual = datetime.now()
        intentos.numero-=1
        intentos.save()

        calificacion = 0

        res1 = request.POST['res1']
        res2 = request.POST['res2']
        res3 = request.POST['res3']
        res4 = request.POST['res4']
        res5 = request.POST['res5']
        res6 = request.POST['res6']
        res7 = request.POST['res7']
        res8 = request.POST['res8']
        res9 = request.POST['res9']
        res10 = request.POST['res10']

        if (res1 == "b"):
            calificacion+=1

        if (res2 == "c"):
            calificacion += 1

        if (res3 == "a"):
            calificacion += 1

        if (res4 == "c"):
            calificacion += 1

        if (res5 == "a"):
            calificacion += 1

        if (res6 == "a"):
            calificacion += 1

        if (res7 == "b"):
            calificacion += 1

        if (res8 == "b"):
            calificacion += 1

        if (res9 == "a"):
            calificacion += 1

        if (res10 == "a"):
            calificacion += 1
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Visualizar los datos de columnas especificas \n 2.-Proyección \n 3.-Toma los registros con condiciones especificas \n 4.-Es la expresión logica usada para realizar comparaciones \n 5.- ==, <>,<,<=,>,>=,AND,OR,NOT \n 6.-Es un caracter comodín que permite buscar patrones \n 7.-Unión \n 8.-Clausula WHERE \n 9.-Llave primaria y llave foranea \n 10.-Deben existir N-1 condiciones de unión",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Visualizar los datos de columnas especificas \n 2.-Proyección \n 3.-Toma los registros con condiciones especificas \n 4.-Es la expresión logica usada para realizar comparaciones \n 5.- ==, <>,<,<=,>,>=,AND,OR,NOT \n 6.-Es un caracter comodín que permite buscar patrones \n 7.-Unión \n 8.-Clausula WHERE \n 9.-Llave primaria y llave foranea \n 10.-Deben existir N-1 condiciones de unión",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })
@login_required
def ejercicio62(request):

    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=13, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 13,
        alumno = alumno
        )

    if(intentos.numero>0):
        query = request.POST['query']
        # print(query)

        calificacion = 0

        q = query.lower()

        queries = q.split(";")

        for queri in queries:
            queri = queri.replace(" ", "")
            queri = queri.replace('\n', "")
            # print(queri)
            if "selectdistinct(department_id)fromdepartments" in queri:
                calificacion += 1.67
                print(1)

            if "selecthire_datefromemployeeswherefirst_name='david'" in queri:
                calificacion += 1.67
                print(2)
            
            if "selectfirst_name,salary,commission_pctfromemployeeswherecommission_pctisnotnull" in queri:
                calificacion += 1.67
                print(3)

            if "selectfirst_name,last_name,hire_date,salaryfromemployeesinnerjoindepartmentsonemployees.department_id=departments.department_idwheredepartments.department_id=20ordepartments.department_id=70ordepartments.department_id=80ordepartments.department_id=100" in queri:
                calificacion += 1.67
                print(4)

            if "selectfirst_name,last_name,hire_date,salaryfromemployeeswherecommission_pctisnullorderbyfirst_name,last_name" in queri:
                calificacion += 1.67
                print(5)

            if "selectfirst_name||','||last_namefromemployeeswherejob_id='sh_clerk'orjob_id='fi_account'andcommission_pctisnullorderbylast_nameasc" in queri:
                calificacion+=1.67
                print(6)



        calificacion=10 if calificacion>10 else round(calificacion, 2)
        intentos.numero-=1
        intentos.save()
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        respuesta, created = Respuesta.objects.get_or_create(
            ejercicio_id = 13,
            alumno = alumno
        )

        respuesta.respuesta=query
        respuesta.save()


        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })
    if(intentos.numero == 0):
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

# NECESARIO EL SERVIDOR SQL DE ORACLE
@login_required
def ejercicio71(request):

    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=15, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 15,
        alumno = alumno
        )

    if(intentos.numero>0):
        query = request.POST['query']

        intentos.numero-=1
        intentos.save()

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=0
        calificacionBD.save()

        respuesta, created = Respuesta.objects.get_or_create(
            ejercicio_id = 15,
            alumno = alumno
        )

        respuesta.respuesta=query
        respuesta.save()

        calificacion = 0
        query = query.lower()
        query_fixed = query.splitlines()
        for query in query_fixed:
            query = query.strip()
            query = query.replace(" ", "")

            if('select*fromcountries;' in query):
                calificacion +=1.43

            if('select*fromregions;' in query):
                calificacion +=1.43
        
            if('select*fromdepartments;' in query):
                calificacion +=1.43

            if('select*fromemployees;' in query):
                calificacion +=1.43

            if('select*fromjob_history;' in query):
                calificacion +=1.43

            if('select*fromjobs;' in query):
                calificacion +=1.43
            
            if('select*fromlocations;' in query):
                calificacion +=1.43

        calificacion=10 if calificacion>10 else round(calificacion, 2)
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos)",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        if(intentos.numero == 0):
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos)",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
                })
        else:
            return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion       
            })
@login_required
def ejercicio72(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=14, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 14,
        alumno = alumno
        )

    if(intentos.numero>0):
        # Creando un nuevo intento
        fechaActual = datetime.now()
        intentos.numero-=1
        intentos.save()

        calificacion = 0

        res1 = request.POST['res1']
        res2 = request.POST['res2']
        res3 = request.POST['res3']
        res4 = request.POST['res4']
        res5 = request.POST['res5']
        res6 = request.POST['res6']
        res7 = request.POST['res7']
        res8 = request.POST['res8']
        res9 = request.POST['res9']
        res10 = request.POST['res10']

        if (res1 == "b"):
            calificacion+=1

        if (res2 == "d"):
            calificacion += 1

        if (res3 == "b"):
            calificacion += 1

        if (res4 == "a"):
            calificacion += 1

        if (res5 == "a"):
            calificacion += 1

        if (res6 == "a"):
            calificacion += 1

        if (res7 == "b"):
            calificacion += 1

        if (res8 == "b"):
            calificacion += 1

        if (res9 == "a"):
            calificacion += 1

        if (res10 == "a"):
            calificacion += 1
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Fechas y numero \n 2.-Todos los anteriores \n 3.-Un valor nulo es un valor no asignado \n 4.-Resultado Nulo \n 5.-Resultado nulo \n 6.-Modifica el nombre de la columna por el deseado \n 7.-Une cadenas de caracteres de diferentes columnas \n 8.-Caracteres extra mostrado en operaciones SELECT \n 9.-DISTINCT \n 10.-Permite visualizar la estructura de una tabla determinada",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Fechas y numero \n 2.-Todos los anteriores \n 3.-Un valor nulo es un valor no asignado \n 4.-Resultado Nulo \n 5.-Resultado nulo \n 6.-Modifica el nombre de la columna por el deseado \n 7.-Une cadenas de caracteres de diferentes columnas \n 8.-Caracteres extra mostrado en operaciones SELECT \n 9.-DISTINCT \n 10.-Permite visualizar la estructura de una tabla determinada",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })
@login_required
def ejercicio81(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=16, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 16,
        alumno = alumno
        )

    if(intentos.numero>0):
        # Creando un nuevo intento
        fechaActual = datetime.now()
        intentos.numero-=1
        intentos.save()

        calificacion = 0

        res1 = request.POST['res1']
        res2 = request.POST['res2']
        res3 = request.POST['res3']
        res4 = request.POST['res4']
        res5 = request.POST['res5']
        res6 = request.POST['res6']
        res7 = request.POST['res7']
        res8 = request.POST['res8']

        if (res1 == "c"):
            calificacion+=1.25

        if (res2 == "c"):
            calificacion += 1.25

        if (res3 == "b"):
            calificacion += 1.25

        if (res4 == "a"):
            calificacion += 1.25

        if (res5 == "c"):
            calificacion += 1.25

        if (res6 == "b"):
            calificacion += 1.25

        if (res7 == "a"):
            calificacion += 1.25

        if (res8 == "c"):
            calificacion += 1.25
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Describe de manera grafica el esquema de una base de datos \n 2.-Tablas: algo del mundo real, como objetos o acciones \n 3.-Columnas: propiedades que contiene una acción u objeto \n 4.-Conexiones: como se conectan los objetos principales \n 5.-Cuantas entidades se relacionan con otras entidades \n 6.-Cuando un campo clave aparece solo una vez en cada tabla \n 7.-CUando un campo clave aparece varias veces en una tabla \n 8.-Cuando varios campos clave aparecen varias veces en una tabla",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Describe de manera grafica el esquema de una base de datos \n 2.-Tablas: algo del mundo real, como objetos o acciones \n 3.-Columnas: propiedades que contiene una acción u objeto \n 4.-Conexiones: como se conectan los objetos principales \n 5.-Cuantas entidades se relacionan con otras entidades \n 6.-Cuando un campo clave aparece solo una vez en cada tabla \n 7.-CUando un campo clave aparece varias veces en una tabla \n 8.-Cuando varios campos clave aparecen varias veces en una tabla",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })
@login_required
def ejercicio82(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=17, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 17,
        alumno = alumno
        )

    if(intentos.numero>0):
        # Creando un nuevo intento
        fechaActual = datetime.now()
        intentos.numero-=1
        intentos.save()

        calificacion = 0

        llaves = json.loads(request.POST['llaves'])
        tamañoLlaves = len(llaves)
        # print(tamañoLlaves)
        calificacionNegativa=(3-tamañoLlaves)*(2) if tamañoLlaves>3 else 0

        print(llaves)
        if('idProveedor' in llaves):
            # print("SI HAY ID PROVEEDOR")
            calificacion += 3.4

        if('idSucursal' in llaves):
            # print("SI HAY ID PROVEEDOR")
            calificacion += 3.4

        if('idCategoria' in llaves):
            # print("SI HAY ID PROVEEDOR")
            calificacion += 3.4

        calificacion = calificacion + calificacionNegativa
        calificacion=10 if calificacion>10 else round(calificacion, 2)
        calificacion=0 if calificacion<0 else round(calificacion, 2)
        
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-c \n 2.-a \n 3.-b \n 4.-c \n 5.-b \n 6.-a \n 7.-b \n 8.-a \n 9.-a \n 10.-c",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        if(intentos.numero == 0):
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-c \n 2.-a \n 3.-b \n 4.-c \n 5.-b \n 6.-a \n 7.-b \n 8.-a \n 9.-a \n 10.-c",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
                })
        else:
            return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion       
            })
@login_required
def ejercicio91(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=18, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 18,
        alumno = alumno
        )

    if(intentos.numero>0):
        # Creando un nuevo intento
        fechaActual = datetime.now()
        intentos.numero-=1
        intentos.save()

        calificacion = 0

        res1 = request.POST['res1']
        res2 = request.POST['res2']
        res3 = request.POST['res3']
        res4 = request.POST['res4']
        res5 = request.POST['res5']
        res6 = request.POST['res6']
        res7 = request.POST['res7']
        res8 = request.POST['res8']
        res9 = request.POST['res9']
        res10 = request.POST['res10']

        if (res1 == "c"):
            calificacion+=1

        if (res2 == "b"):
            calificacion += 1

        if (res3 == "c"):
            calificacion += 1

        if (res4 == "b"):
            calificacion += 1

        if (res5 == "a"):
            calificacion += 1

        if (res6 == "b"):
            calificacion += 1

        if (res7 == "c"):
            calificacion += 1

        if (res8 == "a"):
            calificacion += 1

        if (res9 == "b"):
            calificacion += 1

        if (res10 == "a"):
            calificacion += 1
    if(calificacion>calificacionBD.calificacion):
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        if(intentos.numero > 0):
            return JsonResponse({
                'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
                .format(calificacion, intentos.numero),
                'intentos':intentos.numero,
                'calificacion_calificacion':calificacion
        })
        else:
            return JsonResponse({
                'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Funciones que operan sobre un conjunto de registros \n 2.-Datos numericos \n 3.-Cualquier tipo de dato \n 4.-Devuelve el numero de registros con valores no nulos dada una comparación \n 5.-Devuelve el numero de valores diferentes que también no sean nulos \n 6.-Si, con la función NVL \n 7.-Divide las filas en grupos mas pequeños \n 8.-Cuando en un SELECT hay un campo que no pertenece a una función de grupo \n 9.-Se combina con GROUP BY para restringir los grupos regresados mediante una condicional \n 10.-HAVING solo condiciona los grupos de la clausula GROUP BY",
                'intentos':0,
                'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (2 intentos) \n las respuestas correctas son:\n 1.-Funciones que operan sobre un conjunto de registros \n 2.-Datos numericos \n 3.-Cualquier tipo de dato \n 4.-Devuelve el numero de registros con valores no nulos dada una comparación \n 5.-Devuelve el numero de valores diferentes que también no sean nulos \n 6.-Si, con la función NVL \n 7.-Divide las filas en grupos mas pequeños \n 8.-Cuando en un SELECT hay un campo que no pertenece a una función de grupo \n 9.-Se combina con GROUP BY para restringir los grupos regresados mediante una condicional \n 10.-HAVING solo condiciona los grupos de la clausula GROUP BY",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })
# ACCIONES DEL MAESTRO--------------------------
@login_required
@user_passes_test(lambda user: user.isMaestro()==True)
def dashboard_profesor(request):
    # print("Six2")
    return render(request, 'maestro/dashboard.html')



@login_required
@user_passes_test(lambda user: user.isMaestro()==True)
def respuestas31(request):
    maestro = Profesor.objects.get(usuario=request.user)
    clases = Clase.objects.filter(profesor=maestro)
    alumnos_entregados = Respuesta.objects.filter(
        ejercicio__id=2,
        alumno__clase__in=clases
    )
    return render(request, 'maestro/respuestas31.html', {
        'alumnos':alumnos_entregados,
        'path':'respuestas31'
    })

@login_required
@user_passes_test(lambda user: user.isMaestro())
def getRespuesta31(request, idAlumno):
    maestro = Profesor.objects.get(usuario=request.user)
    clases = Clase.objects.filter(profesor=maestro)

    alumnos_entregados = Respuesta.objects.filter(
        ejercicio__id=6,
        alumno__clase__in=clases
    )

    respuesta = Respuesta.objects.get(
        alumno__id=idAlumno,
        ejercicio__id=6
    )

    calificacionActual = CalificacionEjercicio.objects.get(
        ejercicio__id=6,
        alumno__id=idAlumno
    )

    if request.method == 'POST':
        form = formEjercicio31(request.POST)

        if form.is_valid():
            calificacion = form.cleaned_data['calificacion']
            calificacionActual.calificacion = calificacion
            calificacionActual.save()

            messages.success(request, 'Calificacion actualizada correctamente')

            return render(request, 'maestro/tabla31.html', {
            'form':form,
            'alumnos':alumnos_entregados,
            'alumno':respuesta.alumno,
            'respuesta':json.loads(respuesta.respuesta),
            'path':'respuestas31'
        })
        else:
            return render(request, 'maestro/tabla31.html', {
            'form':form,
            'alumnos':alumnos_entregados,
            'alumno':respuesta.alumno,
            'respuesta':json.loads(respuesta.respuesta),
            'path':'respuestas31'
        })

    else:
        
        form = formEjercicio31(initial={'calificacion':calificacionActual.calificacion})

        return render(request, 'maestro/tabla31.html',{
            'form':form,
            'alumnos':alumnos_entregados,
            'alumno':respuesta.alumno,
            'respuesta':json.loads(respuesta.respuesta),
            'path':'respuestas31'
        })

@login_required
@user_passes_test(lambda user: user.isMaestro())
def getCalificaciones(request):
    maestro = Profesor.objects.get(usuario=request.user)
    clases = Clase.objects.filter(profesor=maestro)

    alumnos = Alumno.objects.filter(clase__in=clases).order_by("usuario__last_name")
    
    print(alumnos)
    return render(request, 'maestro/calificaciones.html', {
        'alumnos':alumnos
    })

@login_required
@user_passes_test(lambda user: user.isMaestro())
def getCalificacionesAlumno(request, idAlumno):
    maestro = Profesor.objects.get(usuario=request.user)
    clases = Clase.objects.filter(profesor=maestro)
    alumnos = Alumno.objects.filter(clase__in=clases).order_by("usuario__last_name")

    calificaciones = CalificacionEjercicio.objects.filter(
        alumno__id=idAlumno
    ).order_by('ejercicio__unidad__id')

    return render(request, 'maestro/calificaciones.html', {
        'alumnos':alumnos,
        'calificaciones':calificaciones
    })

@login_required
@user_passes_test(lambda user: user.isMaestro())
def setCalificacionAlumno(request):
    idCalificacion = request.POST['idCalificacion']
    calificacionAlumno = request.POST['calificacion']
    print(idCalificacion, calificacionAlumno)

    calificacion = CalificacionEjercicio.objects.get(id=idCalificacion)
    calificacion.calificacion = calificacionAlumno
    calificacion.save()

    return HttpResponse("Calificacion actualizada correctamente")

@login_required
@user_passes_test(lambda user: user.isMaestro())
def ejercicios(request):
    maestro = Profesor.objects.get(usuario=request.user)
    clases = Clase.objects.filter(profesor=maestro)

    ejercicios = Ejercicio.objects.filter(
        unidad__parcial__clase__in=clases
    ).order_by('unidad')
    # print(ejercicios)
    return render(request, 'maestro/ejercicios.html', {
        'ejercicios':ejercicios
    })


@login_required
@user_passes_test(lambda user: user.isMaestro())
def actualizarEjercicio(request):
    idEjercicio = request.POST['idEjercicio']
    estado = request.POST['estado']
    value = True if estado=="true" else False

    print(idEjercicio, estado)
    ejercicio = Ejercicio.objects.get(id=idEjercicio)
    ejercicio.is_active=value
    ejercicio.save()

    return HttpResponse("Ejercicio actualizado correctamente")

@login_required
@user_passes_test(lambda user: user.isMaestro())
def actualizarUnidad(request):
    idUnidad = request.POST['idUnidad']
    estado = request.POST['estado']
    value = True if estado=="true" else False

    print(idUnidad, estado)
    unidad = Unidad.objects.get(id=idUnidad)
    unidad.is_active=value
    unidad.save()

    return HttpResponse("Unidad actualizada correctamente")

@login_required
@user_passes_test(lambda user: user.isMaestro())
def addUser(request):
       #template = loader.get_template('export/importar.html')  
    if request.method == 'POST':
        grupo = request.POST['grupo']
        consulta1 = User.objects.all().values_list('id', flat=True).order_by('id')
        lista1 = list(consulta1)    
        usuario_resource = CategoriaResource()
        usuario_resource2 = CategoriaResource2()   
        dataset = Dataset()
     #print(dataset)  
        nuevos_usuarios = request.FILES['xlsxfile']
     #print(nuevas_personas)  
        imported_data = dataset.load(nuevos_usuarios.read())
        longitud = len(dataset)
        result = usuario_resource.import_data(dataset, dry_run=False)
        consulta2 = User.objects.all().values_list('id', flat=True).order_by('id')
        lista2 = list(consulta2) 
        for i in lista2:
            if i in lista1:
                lista1.remove(i)
            else:
                dataset2 = tablib.Dataset(['', i , grupo], headers=['id','usuario', 'clase'])
                result2 = usuario_resource2.import_data(dataset2, dry_run=False) 
    return render(request, 'maestro/addUsers.html')


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
@user_passes_test(lambda user: user.isMaestro())
def unidades(request):
    maestro = Profesor.objects.get(usuario=request.user)
    clases = Clase.objects.filter(profesor=maestro)

    unidades = Unidad.objects.filter(
        parcial__clase__in=clases
    ).order_by('parcial__clase')
    # print(ejercicios)
    return render(request, 'maestro/unidades.html', {
        'unidades':unidades
    })

    


        
    
