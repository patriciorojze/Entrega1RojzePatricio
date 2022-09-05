from django.db import models

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your models here.


def iniciar_sesion(request):
    if request.method == "GET":
        formulario = AuthenticationForm()

        context = {
            "form": formulario
        }

        