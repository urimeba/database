from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from Apps.Clases.models import Unidad, Parcial, Clase
from Apps.Usuarios.models import Alumno, Profesor
from Apps.Ejercicios.models import Ejercicio, Respuesta, Intentos, CalificacionEjercicio
from .forms import formEjercicio31
from django.contrib.auth.decorators import login_required, user_passes_test
import json
from django.contrib import messages
from decimal import Decimal
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import localtime, now

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
    intentos = Intentos.objects.get(ejercicio__id=13, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 13,
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

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

# ID DEL EJERCICIO: 6
@login_required
def ejercicio11(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=6, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 6,
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

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
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
        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

# ID DEL EJERCICIO: 7
@login_required
def ejercicio22(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=7, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
            ejercicio_id = 7,
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

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

# ID DEL EJERCICIO: 8
@login_required
def ejercicio23(request):

    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=8, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 8,
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

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

# ID DEL EJERCICIO: 2
# EJERCICIO DE LA TABLA
@login_required
def ejercicio31(request):

    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=2, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 2,
        alumno = alumno
        )

    if(intentos.numero>0):
        tabla = request.POST['tabla']
        print(tabla)

        intentos.numero-=1
        intentos.save()

        calificacionBD.fecha = localtime(now())
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
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacionBD.calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

@login_required
def ejercicio32(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=9, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 9,
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

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

@login_required
def ejercicio41(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=10, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 10,
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

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

@login_required
def ejercicio42(request):
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
        atributosPrestamo = json.loads(request.POST['atributosPrestamo'])
        tamañoAtributos = len(atributosPrestamo)
        calificacionNegativa=(6-tamañoAtributos)*(0.5) if tamañoAtributos>6 else 0

        calificacion+=1.67 if 'PK - ID(number)' in atributosPrestamo else 0
        calificacion+=1.67 if 'FK - expedienteAlumno(number)' in atributosPrestamo else 0
        calificacion+=1.67 if 'FK - isbn(varchar2)' in atributosPrestamo else 0
        calificacion+=1.67 if 'FK - claveEmpleado(number)' in atributosPrestamo else 0
        calificacion+=1.67 if 'fechaPrestamo(date)' in atributosPrestamo else 0
        calificacion+=1.67 if 'fechaEntrega(date)' in atributosPrestamo else 0

        calificacion = calificacion - calificacionNegativa
        calificacion=10 if calificacion>10 else round(calificacion, 2)

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

# NECESARIO EL SERVIDOR SQL DE ORACLE
@login_required
def ejercicio51(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=4, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 4,
        alumno = alumno
        )

    if(intentos.numero>0):
        query = request.POST['query']
        print(query)

        intentos.numero-=1
        intentos.save()

        # calificacionBD.fecha = localtime(now())
        # calificacionBD.calificacion=0
        # calificacionBD.save()

        respuesta, created = Respuesta.objects.get_or_create(
            ejercicio_id = 4,
            alumno = alumno
        )
        respuesta.respuesta=query
        respuesta.save()


        return JsonResponse({
            # 'calificacion': "Tu calificacion sera evaluada por tu profesor. (Intentos restantes: {0} intento(s))"
            'calificacion': "TU CALIFICACION SERA ARREGLADA CUANDO EL SERVIDOR ESTE EN LINEA (Intentos restantes: {0} intento(s))"
            .format(intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':1234
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

@login_required
def ejercicio52(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=12, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 12,
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

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

@login_required
def ejercicio61(request):
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

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

@login_required
def ejercicio62(request):

    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=19, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 19,
        alumno = alumno
        )

    if(intentos.numero>0):
        query = request.POST['query']
        print(query)

        intentos.numero-=1
        intentos.save()

        # calificacionBD.fecha = localtime(now())
        # calificacionBD.calificacion=0
        # calificacionBD.save()

        respuesta, created = Respuesta.objects.get_or_create(
            ejercicio_id = 19,
            alumno = alumno
        )

        respuesta.respuesta=query
        respuesta.save()


        return JsonResponse({
            'calificacion': "TU CALIFICACION SERA ARREGLADA CUANDO EL SERVIDOR ESTE EN LINEA. (Intentos restantes: {0} intento(s))"
            .format(intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':1234
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

# NECESARIO EL SERVIDOR SQL DE ORACLE
@login_required
def ejercicio71(request):

    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=5, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 5,
        alumno = alumno
        )

    if(intentos.numero>0):
        query = request.POST['query']

        intentos.numero-=1
        intentos.save()

        # calificacionBD.fecha = localtime(now())
        # calificacionBD.calificacion=0
        # calificacionBD.save()

        respuesta, created = Respuesta.objects.get_or_create(
            ejercicio_id = 5,
            alumno = alumno
        )

        respuesta.respuesta=query
        respuesta.save()


        return JsonResponse({
            'calificacion': "TU CALIFICACION SERA ARREGLADA CUANDO EL SERVIDOR ESTE EN LINEA. (Intentos restantes: {0} intento(s))"
            .format(intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':1234
        })
    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

@login_required
def ejercicio72(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=15, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 15,
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

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
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

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

@login_required
def ejercicio82(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    intentos = Intentos.objects.get(ejercicio__id=20, alumno=alumno)
    calificacionBD = CalificacionEjercicio.objects.get(
        ejercicio_id = 20,
        alumno = alumno
        )

    if(intentos.numero>0):
        # Creando un nuevo intento
        fechaActual = datetime.now()
        intentos.numero-=1
        intentos.save()

        calificacion = 0

        llaves = json.loads(request.POST['llaves'])

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

        calificacion=10 if calificacion>10 else round(calificacion, 2)
        print(calificacion)

        

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0,
            'calificacion_calificacion':calificacionBD.calificacion
        })

@login_required
def ejercicio91(request):
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

        calificacionBD.fecha = localtime(now())
        calificacionBD.calificacion=calificacion
        calificacionBD.save()

        return JsonResponse({
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))"
            .format(calificacion, intentos.numero),
            'intentos':intentos.numero,
            'calificacion_calificacion':calificacion
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
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
        'alumnos':alumnos_entregados
    })

@login_required
@user_passes_test(lambda user: user.isMaestro())
def getRespuesta31(request, idAlumno):
    maestro = Profesor.objects.get(usuario=request.user)
    clases = Clase.objects.filter(profesor=maestro)

    alumnos_entregados = Respuesta.objects.filter(
        ejercicio__id=2,
        alumno__clase__in=clases
    )

    respuesta = Respuesta.objects.get(
        alumno__id=idAlumno,
        ejercicio__id=2
    )

    calificacionActual = CalificacionEjercicio.objects.get(
        ejercicio__id=2,
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
        })
        else:
            return render(request, 'maestro/tabla31.html', {
            'form':form,
            'alumnos':alumnos_entregados,
            'alumno':respuesta.alumno,
            'respuesta':json.loads(respuesta.respuesta)
        })

    else:
        
        form = formEjercicio31(initial={'calificacion':calificacionActual.calificacion})

        return render(request, 'maestro/tabla31.html',{
            'form':form,
            'alumnos':alumnos_entregados,
            'alumno':respuesta.alumno,
            'respuesta':json.loads(respuesta.respuesta)
        })

@login_required
@user_passes_test(lambda user: user.isMaestro())
def getCalificaciones(request):
    maestro = Profesor.objects.get(usuario=request.user)
    clases = Clase.objects.filter(profesor=maestro)

    alumnos = Alumno.objects.filter(clase__in=clases)
    
    print(alumnos)
    return render(request, 'maestro/calificaciones.html', {
        'alumnos':alumnos
    })

@login_required
@user_passes_test(lambda user: user.isMaestro())
def getCalificacionesAlumno(request, idAlumno):
    maestro = Profesor.objects.get(usuario=request.user)
    clases = Clase.objects.filter(profesor=maestro)
    alumnos = Alumno.objects.filter(clase__in=clases)

    calificaciones = CalificacionEjercicio.objects.filter(
        alumno__id=idAlumno
    ).order_by('ejercicio__unidad').order_by('id')

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

