from django.shortcuts import render

# Create your views here.
def compilador(request):
    return render(request, 'compilador.html')
