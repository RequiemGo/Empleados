from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
    """Form definition for Persona."""

    class Meta:
        """Meta definition for Personaform."""

        model = Persona
        fields = ('first_name', 'last_name', 'job',
                  'departamento', 'avatar', 'habilidades')
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
