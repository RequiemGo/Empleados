from django.db.models import query
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from applications import persona
from django.urls import reverse_lazy

from applications.departamento.models import Departamento
# models
from .models import Habilidades, Persona
from .forms import PersonaForm


class InicioView(TemplateView):
    '''vista que carga la pagina de inicio'''
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    #model = Persona
    paginate_by = 5

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Persona.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    model = Persona
    ordering = 'first_name'
    paginate_by = 5


class ListByArea(ListView):
    template_name = 'persona/list_by_area.html'
    model = Persona

    def get_queryset(self):
        area = self.kwargs['short_name']
        lista = Persona.objects.filter(
            departamento__short_name=area
        )
        return lista


class ListByTrabajo(ListView):
    template_name = 'persona/list_by_trabajo.html'
    model = Persona

    def get_queryset(self):
        trabajo = self.kwargs['job']
        lista = Persona.objects.filter(
            job=trabajo
        )
        return lista


class ListEmpleadosByKword(ListView):
    # lista empleados por palabra clave
    template_name = 'persona/by_kword.html'
    context_object_name = 'Empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Persona.objects.filter(
            first_name=palabra_clave
        )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        idempleado = self.request.GET.get('idemple', '')
        persona = Persona.objects.get(id=5)
        '''
        lista = Persona.objects.filter(
            habilidades=idempleado
        )
        '''
        return persona.habilidades.all()
        # lista


class EmpleadoDetailView(DetailView):
    model = Persona
    template_name = "persona/detail_view.html"


class SuccessRegister(TemplateView):
    template_name = 'persona/success.html'


class PersonaCreateView(CreateView):
    model = Persona
    template_name = "persona/create_view.html"
    form_class = PersonaForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(PersonaCreateView, self).form_valid(form)


class PersonaUpdateView(UpdateView):
    model = Persona
    template_name = "persona/update.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')


class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')
