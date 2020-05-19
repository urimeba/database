from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from Apps.Clases.models import Unidad, Parcial
from Apps.Usuarios.models import Alumno
from Apps.Ejercicios.models import Ejercicio, Respuesta, Intentos, CalificacionEjercicio
from django.contrib.auth.decorators import login_required, user_passes_test
import json

# Create your views here.
@login_required
def ejercicio(request, pk, id):
    alumno = Alumno.objects.get(usuario=request.user.id)
    parciales = Parcial.objects.filter(clase=alumno.clase)
    unidades = Unidad.objects.filter(parcial__in=parciales)
    ejercicios = Ejercicio.objects.filter(unidad__id=pk)

    try:
        unidad = Unidad.objects.get(pk=pk)
    except:
        return redirect('dashboard')

    try:
        ejercicio = Ejercicio.objects.get(id=id, unidad=unidad)
        alumno = Alumno.objects.get(usuario__id=request.user.id)
        numeroIntentos, created = Intentos.objects.get_or_create(ejercicio=ejercicio, alumno=alumno)
    except:
        return redirect('dashboard')

    
    return render(request, str(ejercicio.archivo),{
        'ejercicio_seleccionado':ejercicio,
        'unidades': unidades, 
        'ejercicios':ejercicios,
        'intentos': str(numeroIntentos.numero)
    })

# ID DEL EJERCICIO: 6
@login_required
def ejercicio11(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=6, alumno=alumno)

    if(intentos.numero>0):
        # Creando un nuevo intento
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


        calificacionBD, created = CalificacionEjercicio.objects.get_or_create(
            ejercicio_id = 6,
            alumno = alumno
        )

        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0
        })

# ID DEL EJERCICIO: 3
@login_required
def ejercicio21(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=3, alumno=alumno)

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

        calificacionBD, created = CalificacionEjercicio.objects.get_or_create(
            ejercicio_id = 3,
            alumno = alumno
        )
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0
        })

# ID DEL EJERCICIO: 7
@login_required
def ejercicio22(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=7, alumno=alumno)

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

        calificacionBD, created = CalificacionEjercicio.objects.get_or_create(
            ejercicio_id = 7,
            alumno = alumno
        )
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0
        })

# ID DEL EJERCICIO: 8
@login_required
def ejercicio23(request):

    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=8, alumno=alumno)

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

        calificacionBD, created = CalificacionEjercicio.objects.get_or_create(
            ejercicio_id = 8,
            alumno = alumno
        )
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0
        })

# ID DEL EJERCICIO: 2
@login_required
def ejercicio31(request):

    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=2, alumno=alumno)

    if(intentos.numero>0):
        tabla = request.POST['tabla']
        print(tabla)

        intentos.numero-=1
        intentos.save()

        calificacionBD, created = CalificacionEjercicio.objects.get_or_create(
            ejercicio_id = 2,
            alumno = alumno
        )
        calificacionBD.calificacion=0
        calificacionBD.save()


        respuesta, created = Respuesta.objects.get_or_create(
            ejercicio_id = 2,
            alumno = alumno
        )

        respuesta.respuesta=tabla
        respuesta.save()


        return JsonResponse({
            'calificacion': "Tu calificacion sera evaluada por tu profesor. (Intentos restantes: {0} intento(s))"
            .format(intentos.numero),
            'intentos':intentos.numero
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0
        })

@login_required
def ejercicio51(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=4, alumno=alumno)

    if(intentos.numero>0):
        query = request.POST['query']
        print(query)

        intentos.numero-=1
        intentos.save()

        # calificacionBD, created = CalificacionEjercicio.objects.get_or_create(
        #     ejercicio_id = 4,
        #     alumno = alumno
        # )
        # calificacionBD.calificacion=0
        # calificacionBD.save()

        # respuesta, created = Respuesta.objects.get_or_create(
        #     ejercicio_id = 4,
        #     alumno = alumno
        # )

        # respuesta.respuesta=tabla
        # respuesta.save()


        return JsonResponse({
            'calificacion': "Tu calificacion sera evaluada por tu profesor. (Intentos restantes: {0} intento(s))"
            .format(intentos.numero),
            'intentos':intentos.numero
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0
        })


@login_required
def ejercicio71(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=5, alumno=alumno)

    if(intentos.numero>0):
        query = request.POST['query']
        print(query)

        intentos.numero-=1
        intentos.save()

        # calificacionBD, created = CalificacionEjercicio.objects.get_or_create(
        #     ejercicio_id = 5,
        #     alumno = alumno
        # )
        # calificacionBD.calificacion=0
        # calificacionBD.save()

        # respuesta, created = Respuesta.objects.get_or_create(
        #     ejercicio_id = 5,
        #     alumno = alumno
        # )

        # respuesta.respuesta=tabla
        # respuesta.save()


        return JsonResponse({
            'calificacion': "Tu calificacion sera evaluada por tu profesor. (Intentos restantes: {0} intento(s))"
            .format(intentos.numero),
            'intentos':intentos.numero
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0
        })