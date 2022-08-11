
from email.policy import default
from optparse import Option
from random import choices
from django.forms import Form, IntegerField, CharField, EmailField, DateField, FloatField, DateTimeField


class TipoPlanFormulario(Form):
    NroPlan = IntegerField()
    NombrePlan = CharField(max_length=30)
    MaxPersonas = IntegerField()

class PlanFormulario(Form):
    CodigoPlan = CharField()
    FechaAfiliacion = DateField()
    TipoPlan = IntegerField()

class PacienteFormulario(Form):
    
    DNI = IntegerField()
    Nombre = CharField(max_length=45)
    Apellido = CharField(max_length=45)
    FechaNacimiento = DateField()
    Genero = CharField(max_length=10)
    Direccion = CharField(max_length=60)
    Telefono = CharField(max_length=20)

class AfiliacionFormulario(Form):
    DNI = IntegerField()
    CodigoPlan = CharField(max_length=15)
    FechaInicio = DateField()

class PagoFormulario(Form):
    CodigoPlan = CharField(max_length=15)
    FechaPago = DateField()
    Monto = FloatField()

class EspecialidadFormulario(Form):
    CodigoEspecialidad = IntegerField()
    NombreEspecialidad = CharField(max_length=20)

class MedicoFormulario(Form):
    NroMedico = IntegerField()
    Nombre = CharField(max_length=45)
    Apellido = CharField(max_length=45)
    CodigoEspecialidad = IntegerField()

class CitaFormulario(Form):
    DNI = IntegerField()
    NroMedico = IntegerField()
    FechaHora = DateTimeField()


class HistoriaClinicaFormulario(Form):
    NroMedico = IntegerField()
    DNI = IntegerField()
    Notas = CharField(max_length=1600)