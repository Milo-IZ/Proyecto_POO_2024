from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from investigaciones.models import Contenido, MATERIA_CHOICES, ANO_CHOICES


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
    contenido = Contenido.objects.all()
    materia_choices = MATERIA_CHOICES
    ano_choices = ANO_CHOICES

    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        contenido_text = request.POST['contenido']
        autor = request.POST['autor']
        imagen = request.POST['imagen']
        ano = request.POST['ano']
        materia = request.POST['materia']
        articulo = Contenido.objects.create(titulo=titulo, descripcion=descripcion, contenido=contenido_text, autor=autor, imagen=imagen, ano=ano, materia=materia)
        articulo.save()
        return redirect('foro')  # redirect to the same page after submitting the form

    context = {
        'contenido': contenido,
        'materia_choices': materia_choices,
        'ano_choices': ano_choices
    }
    return render(request, "foro.html", context)

    
    


