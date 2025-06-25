from django.urls import path
from . import views

urlpatterns = [
    path('trabajador/listar/', views.TrabajadorListView.as_view(), name='trabajador-listar'),  # Solo lectura
    path('trabajador/crear/', views.TrabajadorCreateView.as_view(), name='trabajador-crear'),  # Crear
    path('trabajador/editar/<int:pk>/', views.TrabajadorUpdateView.as_view(), name='trabajador-editar'),  # Editar
    path('trabajador/eliminar/<int:pk>/', views.TrabajadorDeleteView.as_view(), name='trabajador-eliminar'),  # Confirmar eliminar
]