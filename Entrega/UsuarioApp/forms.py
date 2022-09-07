from django.forms import Form, CharField, EmailField, PasswordInput, ImageField
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class AuthenticationCustomForm(AuthenticationForm):
    username = CharField(label= "Usuario")
    password = CharField(label= "Contraseña", widget= PasswordInput)

    class Meta:
        model = User


class UserCustomForm(UserCreationForm):
    username = CharField(label= "Elija un nombre de usuario")
    email = EmailField(label="Elija un correo electrónico")
    password1 = CharField(label= "Elija una contraseña", widget=PasswordInput)
    password2 = CharField(label= "Escriba nuevamente la contraseña", widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            "username": "150 caracteres o menos. Solo letras, dígitos o  @/./+/-/_ .",
            "password1": "Su contraseña no puede similar a su información personal. \nDebe tener al menos 8 caracteres. \nNo debe se de uso común. \nNo puede ser enteramente numérica",
            "email": "", "password2": "",
        }

class UserPasswordForm(UserCreationForm):
    password1 = CharField(label= "Elija una contraseña", widget=PasswordInput)
    password2 = CharField(label= "Escriba nuevamente la contraseña", widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ["password1", "password2"]
        help_texts = {
            "password1": "Su contraseña no puede similar a su información personal. \nDebe tener al menos 8 caracteres. \nNo debe se de uso común. \nNo puede ser enteramente numérica",
            "password2": "",
        }

class AvatarForm(Form):
    imagen = ImageField()