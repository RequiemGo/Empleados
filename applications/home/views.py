from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView
from .forms import PruebaForm
from applications.home.models import Prueba


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['andres', 'carlos', 'angie', 'monica', 'daniel']


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '/'
