from django.forms import ModelForm
from django import forms
from .models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'appaterno',
            'apmaterno',
            'fechanacimiento',
            'rfc',
            'curp',
            'generoid',
            'celular',
            'telefono',
            'correo',
            'codigopostal',
            'pais',
            'estado',
            'municipio',
            'ciudad',
            'colonia',
            'calle',
            'numcasa'
        ]
        widgets = {
            'fechanacimiento': forms.DateInput(attrs={'type': 'date'})
        }
