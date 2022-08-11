from django.urls import path
from EntregaApp.views import *
from EntregaApp.models import *

urlpatterns = [
    path("base/", pagina_base, name="pagina_base"),
    path("crear/", formulario_lista, name="formulario_lista"),
    path("ver/", informe_lista, name="informe_lista"),
    path("buscar/", buscar_lista, name="buscar_lista"),
    path("ver/tipoplan/", ver_TipoPlan, name="ver_tipoplan"),
    path("crear/tipoplan/", crear_TipoPlan, name="crear_tipoplan"),
    path("ver/paciente/", ver_Paciente, name="ver_paciente"),
    path("crear/paciente/", crear_Paciente, name="crear_paciente"),
    path("ver/plan/", ver_Plan, name="ver_plan"),
    path("crear/plan/", crear_Plan, name="crear_plan"),
    path("ver/afiliacion/", ver_Afiliacion, name="ver_afiliacion"),
    path("crear/afiliacion/", crear_Afiliacion, name="crear_afiliacion"),
    path("ver/pago/", ver_Pago, name="ver_pago"),
    path("crear/pago/", crear_Pago, name="crear_pago"),
    path("ver/especialidad/", ver_Especialidad, name="ver_especialidad"),
    path("crear/especialidad/", crear_Especialidad, name="crear_especialidad"),
    path("ver/medico/", ver_Medico, name="ver_medico"),
    path("crear/medico/", crear_Medico, name="crear_medico"),
    path("ver/cita/", ver_Cita, name="ver_cita"),
    path("crear/cita/", crear_Cita, name="crear_cita"),
    path("ver/cita/", ver_Cita, name="ver_cita"),
    path("crear/cita/", crear_Cita, name="crear_cita"),
    path("ver/historia/", ver_HistoriaClinica, name="ver_historia"),
    path("crear/historia/", crear_HistoriaClinica, name="crear_historia"),
    path("buscar/paciente/", buscar_paciente_form, name="buscar_paciente"),
    path("resultado/paciente/", buscar_paciente, name="resultado_paciente")
]