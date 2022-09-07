from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Mensaje(models.Model):
    usuario1 = models.IntegerField()
    usuario2 = models.IntegerField()
    fecha = models.DateTimeField()
    mensaje = models.CharField(max_length=1400)


        