from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidade'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + '.' + self.habilidad


class Persona(models.Model):
    JOB_CHOICES = [('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'),
                   ('2', 'ECONOMISTA'), ('3', 'DESARROLLADOR'), ('4', 'OTRO')]
    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField('Nombre Completo', max_length=100, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    #hoja_vida = RichTextField(blank=True)
    avatar = models.ImageField(
        'Foto', upload_to='empleado', blank=True, null=True)

    class Meta:
        verbose_name = 'Trabajadore'
        ordering = ['id']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return str(self.id) + '.'+self.first_name + ' ' + self.last_name
