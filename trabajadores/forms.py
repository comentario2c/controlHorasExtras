from django import forms
from .models import Trabajador

class CrearEditarTrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['Nombre','fecha_contrato', 'monto_base', 'bono_produccion']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del trabajador'}),
            'fecha_contrato': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de contrato', 'type': 'date'}),
            'monto_base': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto base'}),
            'bono_produccion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bono de producción'}),
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
