from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from investigaciones.models import Contenido

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        name = request.POST["username"]
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        
        if user is not None:
            auth_login(request, user)  # Iniciar sesión
            return redirect('foro/')  # Redirigir al foro
        else:
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': 'Usuario o contraseña incorrectos'})


def register(request):
    if request.method=='GET':
        return render(request, 'register.html', {'form': UserCreationForm})
    else:
        
        if request.POST["password1"]!=request.POST["password2"]:
            return render(request, 'register.html', {'form': UserCreationForm, 'error': 'Las contraseñas no coinciden'})
        else:
            user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
            user.save()
            return render(request, 'register.html', {'form': UserCreationForm, 'valor': 'Usuario creado correctamente'})


def foro(request):
    contenido=Contenido.objects.all()
    return render(request, "foro.html", {'contenido': contenido},)
    


