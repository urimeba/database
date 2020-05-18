from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from Apps.Clases.models import Unidad, Parcial
from Apps.Usuarios.models import Alumno
from Apps.Ejercicios.models import Ejercicio, Respuesta, Pregunta, Intentos, CalificacionEjercicio
from django.contrib.auth.decorators import login_required, user_passes_test
import json

# Create your views here.
@login_required
def ejercicios(request):
    alumno = Alumno.objects.get(usuario=request.user.id)
    parciales = Parcial.objects.filter(clase=alumno.clase)
    unidades = Unidad.objects.filter(parcial__in=parciales, is_active=True)

    if(alumno.clase.is_active):
        if(unidades.count() > 0):
            idUltimaUnidad = unidades.last().id

            try:
                ejercicio = Ejercicio.objects.filter(unidad__id=idUltimaUnidad).last()
                return redirect('ejercicio', pk=idUltimaUnidad, id=ejercicio.id)
            except:
                return redirect('unidades')
            
        else:
            return render(request, 'actividadesEjercicios.html')
    else:
        return redirect('dashboard')


    return render(request, 'actividadesEjercicios.html')


@login_required
def ejercicio(request, pk, id):
    alumno = Alumno.objects.get(usuario=request.user.id)
    parciales = Parcial.objects.filter(clase=alumno.clase)
    unidades = Unidad.objects.filter(parcial__in=parciales)
    ejercicios = Ejercicio.objects.filter(unidad__id=pk)

    try:
        unidad = Unidad.objects.get(pk=pk)
    except:
        ultima_unidad = Unidad.objects.all().last()
        return redirect('unidad', pk=ultima_unidad.id)

    try:
        ejercicio = Ejercicio.objects.get(id=id)
        alumno = Alumno.objects.get(usuario__id=request.user.id)
        numeroIntentos = Intentos.objects.filter(ejercicio=ejercicio, alumno=alumno).count()
    except:
        ultima_unidad = Unidad.objects.all().last()
        return redirect('unidad', pk=ultima_unidad.id)

    
    return render(request, str(ejercicio.archivo),{
        'ejercicio_seleccionado':ejercicio,
        'unidades': unidades, 
        'ejercicios':ejercicios,
        'intentos': str(3-numeroIntentos)
    })

    

    

@login_required
def setRespuestas(request):
    respuestas = request.POST.get('respuestas')
    idEjercicio = request.POST.get('idEjercicio')
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    ejercicio = Ejercicio.objects.get(id=idEjercicio)
    pregunta = Pregunta.objects.get(ejercicio__id=idEjercicio)

    numeroIntentos = Intentos.objects.filter(ejercicio__id=idEjercicio, alumno=alumno).count()
    print(numeroIntentos)
    if(numeroIntentos<=2):
        
        Intentos.objects.create(ejercicio=ejercicio, alumno=alumno)

        respuestas = json.loads(respuestas)
        for respuesta in respuestas:
            Respuesta.objects.create(pregunta=pregunta, alumno=alumno, respuesta=respuesta)

        return HttpResponse("Respuesta enviadas correctamente")
    else:
        return HttpResponse("Has alcanzado el numero de intentos maximo para este ejercicio")

def pruebas(request):
    return render(request, 'pruebas.html')

# EJERCICIO 1 DE LA UNIDAD 1
# ID DEL EJERCICIO: 6
def ejercicio11(request):
    alumno = Alumno.objects.get(usuario__id=request.user.id)
    numeroIntentos = Intentos.objects.filter(ejercicio__id=6, alumno=alumno).count()

    if(numeroIntentos<3):
        # Creando un nuevo intento
        Intentos.objects.create(
            ejercicio_id=6,
            alumno=alumno
        )

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
            'calificacion': "Tu calificacion ha sido: {0}. (Intentos restantes: {1} intento(s))".format(calificacion, 3-(numeroIntentos+1)),
            'intentos':3-(numeroIntentos+1)
        })

    else:
        return JsonResponse({
            'calificacion': "Has superado el limite de intentos del ejercicio (3 intentos)",
            'intentos':0
        })