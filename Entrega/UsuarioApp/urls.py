from django.urls import path
from UsuarioApp.views import *
from EntregaApp.models import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("base2/", pagina_base2, name="base2"),
    path("login/", iniciar_sesion, name="iniciar_sesion"),
    path("login/exito", usuario_exito_entrada, name="usuario_exito_entrada"),
    path("login/fallo", usuario_fallo_entrada, name="usuario_fallo_entrada"),
    path("registro/", registrar_usuario, name = "registrar_usuario"),
    path("logout/", LogoutView.as_view(template_name = "logout.html"), name="logout"),
    path("contrasena/", modificar_contrasena, name="modificar_contrasena"),
    path("avatar/", crear_avatar, name="crear_avatar")
]

