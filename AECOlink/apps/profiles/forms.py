from django import forms
from apps.profiles.models import *


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = [
            'nombre',
            'password',
            'email',
        ]
        labels = {
            'nombre': 'Nombre y apellidos',
            'password': 'Contraseña',
            'email': 'email',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfesionalesForm(forms.ModelForm):

    class Meta:
        model = Profesional
        fields = [
            'nombre',
            'password',
            'email',
        ]
        labels = {
            'nombre': 'Nombre y apellidos',
            'password': 'Contraseña',
            'email': 'email',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = [
            'nombre',
            'password',
        ]
        labels = {
            'nombre': 'Nombre y apellidos',
            'password': 'Contraseña',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }
