from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view()),
    path('resume/', views.ResumeFoundationView.as_view(), name='resume_foundation'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
