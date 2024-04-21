# forms.py
from django import forms
from .models import Transaccion

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['orden', 'monto_total', 'metodo_pago', 'estado_pago']
        widgets = {
            'estado_pago': forms.Select(choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado')])  # Definir las opciones que desees
        }

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)

    email=forms.CharField(label="Email", required=True)

    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)
