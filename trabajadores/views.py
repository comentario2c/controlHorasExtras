from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import Trabajador
from .forms import crearEditarTrabajadorForm
from django.contrib import messages

# Vista para crear un nuevo trabajador
class TrabajadorCreateView(CreateView):
    model = Trabajador
    form_class = crearEditarTrabajadorForm
    template_name = 'horas_extras/crearTrabajador.html' # Cambiar a la ruta correcta del template

    def form_valid(self, form):
        response = super().form_valid(form)
        trabajador = form.instance  # Este es el objeto recién guardado

        messages.success(
            self.request,
            f"Se ha ingresado el trabajador {trabajador.Nombre} con un monto base de {trabajador.monto_base}$ y un bono de producción de {trabajador.bono_produccion}$ correctamente."
        )
        return response

# Vista para editar un trabajador existente
class TrabajadorUpdateView(UpdateView):
    model = Trabajador
    form_class = crearEditarTrabajadorForm  
    template_name = 'horas_extras/formulario.html' # Cambiar a la ruta correcta del template

    def form_valid(self, form):
        response = super().form_valid(form)
        trabajador = form.instance
        messages.success(
            self.request,
            f"Se ha editado el trabajador {trabajador.Nombre} con un monto base de {trabajador.monto_base}$ y un bono de producción de {trabajador.bono_produccion}$ correctamente."
        )
        return response

# Vista para listar todos los trabajadores
class TrabajadorListView(ListView):
    model = Trabajador
    template_name = 'trabajadores/listarTrabajadores.html' # Cambiar a la ruta correcta del template
    context_object_name = 'trabajadores'

# Vista para eliminar un trabajador
class TrabajadorDeleteView(DeleteView):
    model = Trabajador
    template_name = 'horas_extras/confirmar_eliminacion.html' # Cambiar a la ruta correcta del template

    def delete(self, request, *args, **kwargs):
        trabajador = self.get_object()
        messages.success(
            self.request,
            f"Se ha eliminado el trabajador {trabajador.Nombre} correctamente."
        )
        return super().delete(request, *args, **kwargs)