
from email.policy import default
from optparse import Option
from random import choices
from django.forms import Form, IntegerField, CharField, EmailField, DateField, FloatField, DateTimeField, DateTimeInput, ChoiceField, DateInput


from EntregaApp.models import TipoPlan, Paciente, Plan, Especialidad, Medico
from EntregaApp.widgets import DatePickerInput, DateTimePickerInput

class DatePickerInput(DateInput):
    input_type = 'date'

class TipoPlanFormulario(Form):
    NroPlan = IntegerField(label="Número de plan")
    NombrePlan = CharField(max_length=30, label="Nombre del plan")
    MaxPersonas = IntegerField(label="Máximo de afiliados permitido")

TipoPlanesGet = TipoPlan.objects.all()
TipoPlanesChoices = []

for tipo in TipoPlanesGet:
    TipoPlanesChoices.append((tipo.NroPlan, tipo.NombrePlan))

class PlanFormulario(Form):
    CodigoPlan = CharField(label="Código del plan")
    FechaAfiliacion = DateField(label="Fecha de afiliación", widget= DatePickerInput())
    TipoPlan = ChoiceField(choices= TipoPlanesChoices, label = "Tipo de plan")

Generos = [('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')]
class PacienteFormulario(Form):    
    DNI = IntegerField(label="DNI")
    Nombre = CharField(max_length=45)
    Apellido = CharField(max_length=45)
    FechaNacimiento = DateField(
        label="Fecha de Nacimiento", 
        widget = DatePickerInput()
        )
    Genero = ChoiceField(choices= Generos, label= "Género")
    Direccion = CharField(max_length=60, label="Dirección")
    Telefono = CharField(max_length=20, label="Teléfono")

PlanesGet = Plan.objects.all()
PlanesChoices = []

for planlista in PlanesGet:
    PlanesChoices.append((planlista.CodigoPlan, planlista.CodigoPlan))

PacientesGet = Paciente.objects.all()
PacientesChoices = []

for pacientelista in PacientesGet:
    NombreCompleto = pacientelista.Apellido + ', ' + pacientelista.Nombre
    PacientesChoices.append((pacientelista.DNI, NombreCompleto))

class AfiliacionFormulario(Form):
    DNI = ChoiceField(choices = PacientesChoices, label = "Paciente")
    CodigoPlan = ChoiceField(choices= PlanesChoices, label ="Código de Plan")
    FechaInicio = DateField(label="Fecha de inicio", widget= DatePickerInput())

class PagoFormulario(Form):
    CodigoPlan = ChoiceField(choices= PlanesChoices, label ="Código de Plan")
    FechaPago = DateField(label="Fecha de pago", widget= DatePickerInput())
    Monto = FloatField()

class EspecialidadFormulario(Form):
    CodigoEspecialidad = IntegerField(label="Código de la especialidad")
    NombreEspecialidad = CharField(max_length=20, label="Nombre de la especialidad")

EspecialidadesGet = Especialidad.objects.all()
EspecialidadesChoices = []
for tipo in EspecialidadesGet:
    EspecialidadesChoices.append((tipo.CodigoEspecialidad, tipo.NombreEspecialidad))

class MedicoFormulario(Form):
    NroMedico = IntegerField(label="Número de médico")
    Nombre = CharField(max_length=45)
    Apellido = CharField(max_length=45)
    CodigoEspecialidad = ChoiceField(choices = EspecialidadesChoices, label = "Especialidad")

MedicosGet = Medico.objects.all()
MedicosChoices = []
for tipo in MedicosGet:
    NombreCompleto = tipo.Apellido + ', ' + tipo.Nombre
    MedicosChoices.append((tipo.NroMedico, NombreCompleto))
class CitaFormulario(Form):
    DNI = ChoiceField(choices = PacientesChoices, label = "Paciente")
    NroMedico = ChoiceField(choices= MedicosChoices, label='Médico')
    FechaHora = DateTimeField(
        label = "Fecha y hora de la cita",
         widget = DateTimePickerInput())

class HistoriaClinicaFormulario(Form):
    NroMedico = ChoiceField(choices= MedicosChoices, label='Médico')
    DNI = ChoiceField(choices = PacientesChoices, label = "Paciente")
    Notas = CharField(max_length=1600)