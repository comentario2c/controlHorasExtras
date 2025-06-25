from django import forms
from .models import OrdenTrabajo

class OrdenTrabajoForm(forms.ModelForm):
    class Meta:
        model = OrdenTrabajo
        fields = ['ID_OrdenTrabajo', 'Descripcion']
        widgets = {
            'ID_OrdenTrabajo': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
                'min': '0',
                'step': '1',
                'oninput': 'this.value = this.value.replace(/[^0-9]/g, "")',
            }),
            'Descripcion': forms.Textarea(attrs={
                'rows': 5,
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm resize-none focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
        }
