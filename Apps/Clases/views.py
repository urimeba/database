from django.shortcuts import render
from Apps.Clases import forms as forms_clases

# Create your views here.

def home(request):

    if request.method == 'POST':   
        form = forms_clases.Login(request.POST)
        if form.is_valid():
            pass

    else:
        form = forms_clases.Login()


    return render(request, 'login.html', {'form':form})

def compilador(request):
    return render(request, 'compilador.html')
