from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponse
from Apps.Usuarios.models import Alumno
from Apps.Clases.models import Unidad, Parcial
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from django.conf import settings
import json
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
# from .forms import formLogin

# Create your views here.

# class Loginn(LoginView):
#     template_name = 'login.html'
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect(settings.LOGIN_REDIRECT_URL)
#         else:
#             form = formLogin()
#             return render(request, 'login.html', {'form':form})
#         return super().get(request, *args, **kwargs)

@csrf_exempt
def reset_password(request):
    try:
        if request.method == 'POST':
            User = get_user_model()
            old_password = request.POST['old_password']
            new_password = request.POST['new_password1']
            confirm_new_password = request.POST['new_password2']

            if new_password == confirm_new_password:
                if new_password.strip() == '':
                    return messages.success(request, 'La contraseña no puede estar vacia')
                else:
                    if len(new_password) < 6:
                        return JsonResponse({'error': 'La contraseña debe contener mínimo 6 caracteres'})
                    else:
                        usr = User.objects.get(id = request.session['_auth_user_id'])
                        if(usr.check_password(old_password)):
                            usr.set_password(new_password)
                            usr.save()
                            return JsonResponse({'message': 'Las contraseñas ha sido cambiada exitosamente'})

                        return JsonResponse({'message': 'Contraseña antigua incorrecta'})
            else:
                return messages(request, 'Las contraseñas no coinciden')

        return redirect('dashboard')
    except EOFError as identifier:
        return JsonResponse({'error': 'Ha ocurrido un error en el servidor, intentelo nuevamente.'})