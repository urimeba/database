from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, HttpResponse
from Apps.Clases import forms as forms_clases
from Apps.Clases import models as models_clases
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


class Login(LoginView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().get(request, *args, **kwargs)

# # Create your views here.
# def loginn(request):
#     if request.method == 'POST':
#         form = forms_clases.formLogin(request.POST)
#         if form.is_valid():
#             expediente = form.cleaned_data['expediente']
#             password = form.cleaned_data['password']

#             # print(expediente)
#             # print(password)

#             user = authenticate(request, username=expediente, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')
#             else:
#                 messages.add_message(request, messages.ERROR, 'Usuario o contraseña incorrectos')

#     else:
#         form = forms_clases.formLogin()

#     return render(request, 'login.html', {'form':form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def compilator(request):
    return render(request, 'compilador.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

