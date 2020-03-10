from django.shortcuts import render, redirect
from Apps.Clases import forms as forms_clases
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from Apps.Clases import models as models_clases
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':   
        form = forms_clases.formLogin(request.POST)
        if form.is_valid():
            expediente = form.cleaned_data['expediente']
            password = form.cleaned_data['password']

            # print(expediente)
            # print(password)

            user = authenticate(request, username=expediente, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.add_message(request, messages.ERROR, 'Usuario o contraseña incorrectos')

    else:
        form = forms_clases.formLogin()

    return render(request, 'login.html', {'form':form})

def dashboard(request):
    return render(request, 'index.html')

def compilador(request):
    return render(request, 'compilador.html')


