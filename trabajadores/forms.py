from django import forms
from .models import Trabajador

class CrearEditarTrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['Nombre','fecha_contrato', 'monto_base', 'bono_produccion', 'tipo']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-input w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500', 'placeholder': 'Nombre del trabajador'}),
            'fecha_contrato': forms.DateInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500', 'placeholder': 'Fecha de contrato', 'type': 'date'}, format='%Y-%m-%d'),
            'monto_base': forms.NumberInput(attrs={'class': 'form-input w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500', 'style': '-moz-appearance: textfield; -webkit-appearance: none; margin: 0;', 'placeholder': 'Monto base'}),
            'bono_produccion': forms.NumberInput(attrs={'class': 'form-input w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500', 'style': '-moz-appearance: textfield; -webkit-appearance: none; margin: 0;', 'placeholder': 'Bono de producción'}),
            'tipo': forms.TextInput(attrs={'class': 'form-input w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500', 'placeholder': 'Tipo de trabajador'}),
        }
    


    def clean(self):
        cleaned_data = super().clean()
        monto_base = cleaned_data.get('monto_base')
        bono_produccion = cleaned_data.get('bono_produccion')

        if monto_base is not None and monto_base < 0:
            self.add_error('monto_base', 'El monto base no puede ser negativo.')
        if bono_produccion is not None and bono_produccion < 0:
            self.add_error('bono_produccion', 'El bono de producción no puede ser negativo.')

        return cleaned_data
