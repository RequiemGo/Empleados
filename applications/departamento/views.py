from django.shortcuts import render
from django.views.generic.edit import FormView
from applications import departamento
from django.views.generic import ListView
from applications.departamento.models import Departamento
from .forms import NewDepartamentoForm
from applications.persona.models import Persona
# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"


class NewDepartamento(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        depa = Departamento(
            name=form.cleaned_data['departamento'], short_name=form.cleaned_data['short_depar'])
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Persona.objects.create(
            first_name=nombre, last_name=apellidos, job='1', departamento=depa)
        return super(NewDepartamento, self).form_valid(form)
