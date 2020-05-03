from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from Apps.Clases.models import Unidad, Parcial
from Apps.Usuarios.models import Alumno
from Apps.Ejercicios.models import Ejercicio, Respuesta, Pregunta, Intentos
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
    except:
        ultima_unidad = Unidad.objects.all().last()
        return redirect('unidad', pk=ultima_unidad.id)

    
    return render(request, str(ejercicio.archivo),{
        'ejercicio_seleccionado':ejercicio,
        'unidades': unidades, 
        'ejercicios':ejercicios
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