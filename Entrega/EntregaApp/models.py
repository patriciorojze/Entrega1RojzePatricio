from random import choices
from django.db import models
import datetime


# Create your models here.

class TipoPlan(models.Model):
    NroPlan = models.IntegerField(primary_key= True)
    NombrePlan = models.CharField(max_length=30)
    MaxPersonas = models.IntegerField()


class Plan(models.Model):
    CodigoPlan = models.CharField(primary_key=True, max_length=15)
    FechaAfiliacion = models.DateField()
    TipoPlan = models.IntegerField()

class Paciente(models.Model):    
    
    DNI = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
    FechaNacimiento = models.DateField()
    Genero = models.CharField(max_length=10)
    Direccion = models.CharField(max_length=60)
    Telefono = models.CharField(max_length=20)

class Afiliacion(models.Model):
    DNI = models.IntegerField()
    CodigoPlan = models.CharField(max_length=15)
    FechaInicio = models.DateField()
    FechaFin = models.DateField(null=True)

    def Desafiliar(self):
        self.FechaFin = datetime.datetime.now()

class Pago(models.Model):
    CodigoPlan = models.CharField(max_length=15)
    FechaPago = models.DateField()
    Monto = models.FloatField()

class Especialidad(models.Model):
    CodigoEspecialidad = models.IntegerField()
    NombreEspecialidad = models.CharField(max_length=20)

class Medico(models.Model):
    NroMedico = models.IntegerField()
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
    CodigoEspecialidad = models.IntegerField()

class Cita(models.Model):
    DNI = models.IntegerField()
    NroMedico = models.IntegerField()
    FechaHora = models.DateTimeField()
    Cancelada = models.BooleanField()

    def CancelarCita(self):
        self.Cancelada = True
        print("Cita cancelada.")
    
    def Reprogramar(self, NuevaFecha:datetime):
        self.Cancelada = True
        nueva_cita = Cita(DNI = self.DNI, NroMedico = self.NroMedico, FechaHora = NuevaFecha, Cancelada = False)
        nueva_cita.save()
        print("Cita Reprogramada.")

class HistoriaClinica(models.Model):
    NroMedico = models.IntegerField()
    DNI = models.IntegerField()
    FechaNota = models.DateTimeField()
    Notas = models.CharField(max_length=1600)


