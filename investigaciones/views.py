from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from investigaciones.models import Contenido, MATERIA_CHOICES, ANO_CHOICES
from investigaciones.forms import ContenidoForm, DenunciaForm, CommentForm
from django.contrib  import messages
from django.contrib.auth.decorators import login_required
from investigaciones.models import Contenido
from investigaciones.forms import ContenidoForm, DenunciaForm, CommentForm, VotoForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from investigaciones.models import Voto
from django.contrib.auth import logout
from django.contrib import messages




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
    return render(request, "foro.html", {'contenido': contenido})

    
# creando la funcion del boton leer mas de la card en el foro este redirige a la pagina post.html

def crear_contenido(request):
    if request.method == 'POST':
        form = ContenidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foro')
    else:
        form = ContenidoForm()
    return render(request, 'form.html', {'form': form})



def denunciar(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denuncia = form.save(commit=False)  # Create a denuncia instance but don't save it yet
            denuncia.user = request.user  # Set the user field to the currently logged-in user
            denuncia.save()  # Save the denuncia instance
            return redirect('post', id=request.POST.get('contenido_id'))
    else:
        form = DenunciaForm()
        return render(request, 'modal_denuncia.html', {'form': form})
    
    
def post(request, id):
    contenido = Contenido.objects.get(id=id)
    denuncia_form = DenunciaForm(initial={'user': request.user})
    voto_form = VotoForm(initial={'user': request.user})  # Add this line
    return render(request, "post.html", {'contenido': contenido, 'denuncia_form': denuncia_form, 'voto_form': voto_form})  # Add voto_form to the template context

def profile(request):
    return render(request, 'profile.html', {'username': request.user.username})

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')  # Redirigir a la página de inicio de sesión después de cerrar sesión

@login_required
def mis_investigaciones(request):
    user = request.user
    investigaciones = Contenido.objects.filter(autor=user.username)  # Asumiendo que el campo 'autor' almacena el nombre de usuario
    return render(request, 'mis_investigaciones.html', {'investigaciones': investigaciones})

@login_required
def voto(request):
    if request.method == 'POST':
        form = VotoForm(request.POST)
        if form.is_valid():
            voto = form.save(commit=False)
            voto.user = request.user
            contenido_id = request.POST.get('contenido_id')
            voto.contenido = Contenido.objects.get(id=contenido_id)
            voto.save()
            messages.success(request, 'Voto creado con éxito')
            return redirect('post', contenido_id)  # Change the redirect URL
    else:
        form = VotoForm()
    return render(request, 'post.html', {'form': form})
