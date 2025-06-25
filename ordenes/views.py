from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import OrdenTrabajo
from .forms import OrdenTrabajoForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q

# Listado de órdenes
class OrdenListView(ListView):
    model = OrdenTrabajo
    template_name = 'ordenes/listar.html'
    context_object_name = 'ordenes'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(ID_OrdenTrabajo__icontains=query) |
                Q(Descripcion__icontains=query)
            )
        return queryset


# Crear nueva orden
class OrdenCreateView(CreateView):
    model = OrdenTrabajo
    form_class = OrdenTrabajoForm
    template_name = 'ordenes/crear.html'
    success_url = reverse_lazy('orden-listar')

    def form_valid(self, form):
        response = super().form_valid(form)
        orden = form.instance
        messages.success(
            self.request,
            f"Orden creada correctamente para el cliente {orden.ID_OrdenTrabajo} con descripción '{orden.Descripcion}'."
        )
        return response


class OrdenUpdateView(UpdateView):
    model = OrdenTrabajo
    form_class = OrdenTrabajoForm
    template_name = 'ordenes/editar.html'
    success_url = reverse_lazy('orden-listar')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Orden de trabajo actualizada correctamente.")
        return response

# Eliminar orden
class OrdenDeleteView(DeleteView):
    model = OrdenTrabajo
    template_name = 'ordenes/confirmar_eliminar.html'
    success_url = reverse_lazy('orden-listar')

    def delete(self, request, *args, **kwargs):
        orden = self.get_object()
        messages.success(
            self.request,
            f"Orden para el cliente {orden.cliente} eliminada correctamente."
        )
        return super().delete(request, *args, **kwargs)

