
from django.shortcuts import render, redirect
from django.http import HttpResponse
from UsuarioApp.models import Avatar
from UsuarioApp.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def pagina_base2(request):
    context = dict()
    return render(request, "base2.html", context)

def usuario_exito_entrada(request):
    context = {"mensaje": "Usuario válido. Bienvenido/a al Centro Médico Pérez."}
    return render(request, "mensaje2.html", context)

def usuario_fallo_entrada(request):
    context = {"mensaje": "Usuario inválido."}
    return render(request, "mensaje2.html", context)

def iniciar_sesion(request):
    if request.method == "GET":
        formulario = AuthenticationCustomForm()

        context = {
            "form": formulario
        }

        return render(request, "login.html", context)
    
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = authenticate(username = data.get("username"), password=data.get("password"))

            if usuario is not None:
                login(request, usuario)
                return redirect("usuario_exito_entrada")

            else:
                return redirect("usuario_fallo_entrada")
        else:
            return redirect("usuario_fallo_entrada")

def registrar_usuario(request):
    if request.method == "GET":
        formulario = UserCustomForm()
        return render(request, "registro.html", {"form": formulario})
    else: 
        formulario = UserCustomForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request, "mensaje2.html", {"mensaje": "Usuario creado con éxito."})
        else:
            return render(request, "mensaje2.html", {"mensaje": "Error al crear el usuario."})

@login_required
def modificar_contrasena(request):
    if request.method == "GET":
        formulario = UserPasswordForm()
        return render(request, "cambiar_contrasena.html", {"form": formulario})
    else: 
        formulario = UserPasswordForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            usuario = request.user
            if datos.get("password1") is not None:
                if datos.get("password1") != "":
                    if datos.get("password1") == datos.get("password2"):
                        usuario.password1 = datos.get("password1")
                        usuario.password2 = datos.get("password2")

                        usuario.save()
                        return render(request, "mensaje2.html", {"mensaje": "Contraseña modificada con éxito."})
                    else:
                        return render(request, "mensaje2.html", {"mensaje": "Error al modificar la contraseña."})
                else:
                    return render(request, "mensaje2.html", {"mensaje": "Error al modificar la contraseña."})
            else:
                return render(request, "mensaje2.html", {"mensaje": "Error al modificar la contraseña."})
            
        else:
            return render(request, "mensaje2.html", {"mensaje": "Error al modificar la contraseña."})

@login_required
def crear_avatar(request):
    if request.method == "GET":
        formulario = AvatarForm()
        return render(request, "avatar.html", {"form": formulario})
    else: 
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            usuario = User.objects.get(username = request.user.username)
            
            nuevo_Avatar = Avatar(usuario = usuario, imagen = datos["imagen"])
            print(nuevo_Avatar)
            nuevo_Avatar.save()
            return render(request, "mensaje2.html", {"mensaje": "Avatar cargado con éxito."})
        else:
            return render(request, "mensaje2.html", {"mensaje": "Error al cargar el avatar."})
