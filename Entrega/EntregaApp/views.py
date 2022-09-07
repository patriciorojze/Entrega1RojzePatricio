from django.shortcuts import render, redirect
from django.http import HttpResponse
from EntregaApp.forms import *
from EntregaApp.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def pagina_base(request):
    context = dict()
    return render(request, "base.html", context)

def formulario_lista(request):
    return render(request, "formularios_lista.html")

def informe_lista(request):
    return render(request, "informes_lista.html")

def buscar_lista(request):
    return render(request, "buscar_lista.html")

@login_required
def crear_TipoPlan(request):

    if request.method == "GET":
        miFormulario = TipoPlanFormulario()
        return render(request, "formularios.html", {"miFormulario": miFormulario})

    else:

        miFormulario = TipoPlanFormulario(request.POST)
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            NroPlan = datos.get("NroPlan")
            NombrePlan = datos.get("NombrePlan")
            MaxPersonas = datos.get("MaxPersonas")

            nuevo_plan = TipoPlan(NroPlan = NroPlan, NombrePlan = NombrePlan, MaxPersonas = MaxPersonas)
            nuevo_plan.save()

            return redirect('ver_tipoplan')

        else:
            return render(request, "mensaje.html",{"mensaje":"Formulario no válido"})

@login_required
def crear_Paciente(request):

    if request.method == "GET":
        miFormulario = PacienteFormulario()
        return render(request, "formularios.html", {"miFormulario": miFormulario})

    else:

        miFormulario = PacienteFormulario(request.POST)
        print(miFormulario.data.get("FechaNacimiento"))
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            DNI = datos.get("DNI")
            Nombre = datos.get("Nombre")
            Apellido = datos.get("Apellido")
            FechaNacimiento = datos.get("FechaNacimiento")
            Genero = datos.get("Genero")
            Direccion = datos.get("Direccion")
            Telefono = datos.get("Telefono")

            nuevo_paciente = Paciente(DNI = DNI, Nombre = Nombre, Apellido = Apellido, FechaNacimiento = FechaNacimiento, Genero = Genero, Direccion = Direccion, Telefono = Telefono)
            nuevo_paciente.save()

            return redirect('ver_paciente')

        else:
            return render(request, "mensaje.html",{"mensaje":"Formulario no válido"})

@login_required
def crear_Plan(request):

    if request.method == "GET":
        miFormulario = PlanFormulario()
        return render(request, "formularios.html", {"miFormulario": miFormulario})

    else:

        miFormulario = PlanFormulario(request.POST)
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            CodigoPlan = datos.get("CodigoPlan")
            FechaAfiliacion = datos.get("FechaAfiliacion")
            TipoPlan = datos.get("TipoPlan")

            nuevo_plan = Plan(CodigoPlan = CodigoPlan, FechaAfiliacion = FechaAfiliacion, TipoPlan = TipoPlan)
            nuevo_plan.save()

            return redirect('ver_plan')

        else:
            return render(request, "mensaje.html",{"mensaje":"Formulario no válido"})

@login_required
def crear_Afiliacion(request):

    if request.method == "GET":
        miFormulario = AfiliacionFormulario()
        return render(request, "formularios.html", {"miFormulario": miFormulario})

    else:

        miFormulario = AfiliacionFormulario(request.POST)
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            DNI = datos.get("DNI")
            CodigoPlan = datos.get("CodigoPlan")
            FechaInicio = datos.get("FechaInicio")

            nuevo_plan = Afiliacion(DNI = DNI, CodigoPlan = CodigoPlan, FechaInicio = FechaInicio, FechaFin = None)
            nuevo_plan.save()

            return redirect('ver_afiliacion')

        else:
            return render(request, "mensaje.html",{"mensaje":"Formulario no válido"})

@login_required
def crear_Pago(request):

    if request.method == "GET":
        miFormulario = PagoFormulario()
        return render(request, "formularios.html", {"miFormulario": miFormulario})

    else:

        miFormulario = PagoFormulario(request.POST)
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            CodigoPlan = datos.get("CodigoPlan")
            FechaPago = datos.get("FechaPago")
            Monto = datos.get("Monto")

            nuevo_plan = Pago(CodigoPlan = CodigoPlan, FechaPago = FechaPago, Monto = Monto)
            nuevo_plan.save()

            return redirect('ver_pago')

        else:
            return render(request, "mensaje.html",{"mensaje":"Formulario no válido"})

@login_required
def crear_Especialidad(request):

    if request.method == "GET":
        miFormulario = EspecialidadFormulario()
        return render(request, "formularios.html", {"miFormulario": miFormulario})

    else:

        miFormulario = EspecialidadFormulario(request.POST)
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            CodigoEspecialidad = datos.get("CodigoEspecialidad")
            NombreEspecialidad = datos.get("NombreEspecialidad")

            nuevo_plan = Especialidad(CodigoEspecialidad = CodigoEspecialidad, NombreEspecialidad = NombreEspecialidad)
            nuevo_plan.save()

            return redirect('ver_especialidad')

        else:
            return render(request, "mensaje.html",{"mensaje":"Formulario no válido"})

@login_required
def crear_Medico(request):

    if request.method == "GET":
        miFormulario = MedicoFormulario()
        return render(request, "formularios.html", {"miFormulario": miFormulario})

    else:

        miFormulario = MedicoFormulario(request.POST)
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            NroMedico = datos.get("NroMedico")
            Nombre = datos.get("Nombre")
            Apellido = datos.get("Apellido")
            CodigoEspecialidad = datos.get("CodigoEspecialidad")

            nuevo_plan = Medico(NroMedico = NroMedico, Nombre = Nombre, Apellido = Apellido, CodigoEspecialidad = CodigoEspecialidad)
            nuevo_plan.save()

            return redirect('ver_medico')

        else:
            return render(request, "mensaje.html",{"mensaje":"Formulario no válido"})

@login_required
def crear_Cita(request):

    if request.method == "GET":
        miFormulario = CitaFormulario()
        return render(request, "formularios.html", {"miFormulario": miFormulario})

    else:

        miFormulario = CitaFormulario(request.POST)
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            DNI = datos.get("DNI")
            NroMedico = datos.get("NroMedico")
            FechaHora = datos.get("FechaHora")

            nuevo_plan = Cita(DNI = DNI, NroMedico = NroMedico, FechaHora = FechaHora, Cancelada = False)
            nuevo_plan.save()

            return redirect('ver_cita')

        else:
            return render(request, "mensaje.html",{"mensaje":"Formulario no válido"})

@login_required
def crear_HistoriaClinica(request):

    if request.method == "GET":
        miFormulario = HistoriaClinicaFormulario()
        return render(request, "formularios.html", {"miFormulario": miFormulario})

    else:

        miFormulario = HistoriaClinicaFormulario(request.POST)
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            DNI = datos.get("DNI")
            NroMedico = datos.get("NroMedico")
            Notas = datos.get("Notas")

            nuevo_plan = HistoriaClinica(DNI = DNI, NroMedico = NroMedico, FechaNota = datetime.datetime.now(), Notas = Notas)
            nuevo_plan.save()

            return redirect('ver_historia')

        else:
            return render(request, "mensaje.html",{"mensaje":"Formulario no válido"})

def ver_TipoPlan(request):
    planes = TipoPlan.objects.all()
    
    datos = []

    for plan in planes:
        datos.append((plan.NroPlan, plan.NombrePlan))

    context = {
        "titulo": "Lista de tipos de planes disponibles",
        "objetoNombre": "Tipo de plan",
        "datos": datos
    }

    return render(request, "informe.html", context)

@login_required
def ver_Paciente(request):
    planes = Paciente.objects.all()
    
    datos = []

    for plan in planes:
        NombreCompleto = plan.Apellido + ', ' + plan.Nombre
        datos.append((plan.DNI, NombreCompleto))

    context = {
        "titulo": "Lista de pacientes",
        "objetoNombre": "Paciente",
        "datos": datos
    }

    return render(request, "informe.html", context)

@login_required
def ver_Plan(request):
    planes = Plan.objects.all()
    
    datos = []

    for plan in planes:
        DatosCompleto = str(plan.TipoPlan) + ', ' + str(plan.FechaAfiliacion)
        datos.append((plan.CodigoPlan, DatosCompleto))

    context = {
        "titulo": "Lista de planes",
        "objetoNombre": "Plan",
        "datos": datos
    }

    return render(request, "informe.html", context)

@login_required
def ver_Afiliacion(request):
    planes = Afiliacion.objects.all()
    
    datos = []

    for plan in planes:
        datos.append((plan.CodigoPlan, str(plan.DNI)))

    context = {
        "titulo": "Lista de afiliaciones",
        "objetoNombre": "Afiliación",
        "datos": datos
    }

    return render(request, "informe.html", context)

@login_required
def ver_Pago(request):
    planes = Pago.objects.all()
    
    datos = []

    for plan in planes:
        datos.append((plan.CodigoPlan, plan.FechaPago))

    context = {
        "titulo": "Lista de pagos",
        "objetoNombre": "Fecha de pago",
        "datos": datos
    }

    return render(request, "informe.html", context)

def ver_Especialidad(request):
    planes = Especialidad.objects.all()
    
    datos = []

    for plan in planes:
        datos.append((plan.CodigoEspecialidad, plan.NombreEspecialidad))

    context = {
        "titulo": "Lista de especialidades",
        "objetoNombre": "Especialidad",
        "datos": datos
    }

    return render(request, "informe.html", context)

def ver_Medico(request):
    planes = Medico.objects.all()
    
    datos = []

    for plan in planes:
        NombreCompleto = plan.Apellido + ", " + plan.Nombre
        datos.append((plan.NroMedico, NombreCompleto))

    context = {
        "titulo": "Lista de Médicos",
        "objetoNombre": "Nombre Completo",
        "datos": datos
    }

    return render(request, "informe.html", context)

@login_required
def ver_Cita(request):
    planes = Cita.objects.all()
    
    datos = []

    for plan in planes:
        CitaDetalle = str( plan.NroMedico) + ", " + str(plan.DNI)
        datos.append((plan.FechaHora, CitaDetalle))

    context = {
        "titulo": "Lista de Citas",
        "objetoNombre": "Detalle de la cita",
        "datos": datos
    }

    return render(request, "informe.html", context)

@login_required
def ver_HistoriaClinica(request):
    planes = HistoriaClinica.objects.all()
    
    datos = []

    for plan in planes:
        datos.append((plan.FechaNota, plan.DNI))

    context = {
        "titulo": "Lista de Notas de Historia Clínica",
        "objetoNombre": "DNI",
        "datos": datos
    }

    return render(request, "informe.html", context)

@login_required
def buscar_paciente_form(request):
    return render(request, "buscar_paciente.html", context= {"titulo": "Búsqueda de datos del paciente."})

@login_required
def buscar_paciente(request):

    DNI = request.GET.get("DNI", None)

    if not DNI:
        return HttpResponse("No se indicó ningún DNI.")

    try:
        paciente = Paciente.objects.get(DNI = DNI)
        return render(request, "resultado_paciente.html", {"paciente": paciente})
    except:
        return render(request, "mensaje.html", {"mensaje": "Paciente no encontrado"})

@login_required
def buscar_historia_form(request):
    return render(request, "buscar_historia.html", context= {"titulo": "Búsqueda de historias clinicas."})

@login_required
def buscar_historia(request):
    DNI = request.GET.get("DNI", None)

    if not DNI:
        return HttpResponse("No se indicó ningún DNI.")

    try:
        historias = HistoriaClinica.objects.filter(DNI = DNI)
        paciente = Paciente.objects.get(DNI = DNI)
        print(DNI)

        print(paciente.Nombre)
        print(historias)
        print("@@")

        datos = []
        for historia in historias:
            print(historia.NroMedico)
            medicoRedactor = Medico.objects.get(NroMedico = historia.NroMedico)
            datos.append((medicoRedactor.Nombre, medicoRedactor.Apellido, historia.FechaNota, historia.Notas))

        paciente = Paciente.objects.get(DNI = DNI)
        NombreCompleto = paciente.Apellido + ", " + paciente.Nombre
        return render(request, "resultado_historia.html", {"paciente": NombreCompleto, "datos": datos})
    except:
        return render(request, "mensaje.html", {"mensaje": "Paciente no encontrado"})


def datapicker_pagina(request):
    return render(request, "datepicker1.html")

    