
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from UsuarioApp.models import Mensaje

from UsuarioApp.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from avatar.conf import settings
from avatar.forms import PrimaryAvatarForm, UploadAvatarForm
from avatar.models import Avatar
from avatar.signals import avatar_updated
from avatar.utils import invalidate_cache
from avatar.views import _get_avatars, _get_next
import datetime

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
def change_nuevo(
    request,
    extra_context=None,
    next_override=None,
    upload_form=UploadAvatarForm,
    primary_form=PrimaryAvatarForm,
    *args,
    **kwargs,
):
    if extra_context is None:
        extra_context = {}
    avatar, avatars = _get_avatars(request.user)
    if avatar:
        kwargs = {"initial": {"choice": avatar.id}}
    else:
        kwargs = {}
    upload_avatar_form = upload_form(user=request.user, **kwargs)
    primary_avatar_form = primary_form(
        request.POST or None, user=request.user, avatars=avatars, **kwargs
    )
    if request.method == "POST":
        updated = False
        if "choice" in request.POST and primary_avatar_form.is_valid():
            avatar = Avatar.objects.get(id=primary_avatar_form.cleaned_data["choice"])
            avatar.primary = True
            avatar.save()
            updated = True
            invalidate_cache(request.user)
            messages.success(request, _("Se ha cargado exitosamente su avatar."))
        if updated:
            avatar_updated.send(sender=Avatar, user=request.user, avatar=avatar)
        return redirect(next_override or _get_next(request))

    context = {
        "avatar": avatar,
        "avatars": avatars,
        "upload_avatar_form": upload_avatar_form,
        "primary_avatar_form": primary_avatar_form,
        "next": next_override or _get_next(request),
    }
    context.update(extra_context)
    template_name = settings.AVATAR_CHANGE_TEMPLATE or "avatar.html"
    return render(request, template_name, context)

@login_required
def bandeja_de_entrada(request):
    context = dict()
    return render(request,"bandeja_de_entrada.html", context=context)

@login_required
def enviar_mensaje(request):
    if request.method == "GET":
        formulario = MensajeForm()
        return render(request, "mensaje_enviar.html", {"form": formulario})
    else: 
        formulario = MensajeForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            usuario1 = request.user.id
            usuario2 = datos.get("usuario2")
            fecha = datetime.datetime.now()
            mensaje = datos.get("mensaje")
            nuevo_mensaje = Mensaje(usuario1 = usuario1, usuario2 = usuario2, fecha = fecha, mensaje = mensaje)
            nuevo_mensaje.save()
            return render(request, "mensaje2.html", {"mensaje": "Mensaje enviado con éxito."})
        else:
            return render(request, "mensaje2.html", {"mensaje": "Error al enviar el mensaje."})

@login_required
def ver_enviados(request):
    mensajes = Mensaje.objects.filter(usuario1 = request.user.id)

    datos = []

    for mensajeenviado in mensajes:
        usuario2env = mensajeenviado.usuario2
        UsuarioEnviado = User.objects.get(id = usuario2env)
        NombreEnviado = UsuarioEnviado.username
        Fecha = mensajeenviado.fecha
        Texto = mensajeenviado.mensaje
        datos.append((NombreEnviado, Fecha, Texto))

    context = {
        "datos": datos
    }

    return render(request, "mensajes_enviados.html", context)

def ver_recibidos(request):
    mensajes = Mensaje.objects.filter(usuario2 = request.user.id)

    datos = []

    for mensajeenviado in mensajes:
        usuario1env = mensajeenviado.usuario1
        UsuarioRecibido = User.objects.get(id = usuario1env)
        NombreRecibido = UsuarioRecibido.username
        Fecha = mensajeenviado.fecha
        Texto = mensajeenviado.mensaje
        datos.append((NombreRecibido, Fecha, Texto))

    context = {
        "datos": datos
    }

    return render(request, "mensajes_recibidos.html", context)