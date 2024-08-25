from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from investigaciones.models import Contenido, Comment
from investigaciones.forms import ContenidoForm, DenunciaForm, CommentForm, VotoForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render





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
    voto_form = VotoForm(initial={'user': request.user})  
    comment_form = CommentForm()  # Add this line
    comments = Comment.objects.filter(contenido=contenido)  # Add this line

    if request.method == 'POST' and 'comment' in request.POST:  # Add this condition
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.contenido = contenido
            comment.save()
            return redirect('post', id=id)

    return render(request, "post.html", {
        'contenido': contenido, 
        'denuncia_form': denuncia_form, 
        'voto_form': voto_form,
        'comment_form': comment_form,  # Add this line
        'comments': comments  # Add this line
    })

@login_required
def voto(request, contenido_id):
    contenido = Contenido.objects.get(id=contenido_id)
    if request.method == 'POST':
        form = VotoForm(request.POST)
        if form.is_valid():
            voto = form.save(commit=False)
            voto.user = request.user
            voto.contenido = contenido
            voto.save()
            messages.success(request, 'Voto creado con éxito')
            return redirect('post', contenido_id)  # Change the redirect URL
    else:
        form = VotoForm()
    return render(request, 'post.html', {'form': form, 'contenido': contenido})  # Change the template name


