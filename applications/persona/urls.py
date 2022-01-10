from django.contrib import admin
from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('lista-todo-empleados/',
         views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('lista-by-area/<short_name>',
         views.ListByArea.as_view(), name='empleados_area'),
    path('lista-by-trabajo/<job>',
         views.ListByTrabajo.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path('detail-persona/<pk>/',
         views.EmpleadoDetailView.as_view(), name='persona_detail'),
    path('add-persona/', views.PersonaCreateView.as_view(), name='empleado_add'),
    path('success/', views.SuccessRegister.as_view(), name='success'),
    path('update/<pk>/', views.PersonaUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.PersonaDeleteView.as_view(), name='delete'),
    path('lista-empleados-admin',
         views.ListaEmpleadosAdmin.as_view(), name='empleados_admin'),




]
