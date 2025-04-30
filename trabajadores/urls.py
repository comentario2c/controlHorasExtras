from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.TrabajadorListView.as_view(), name='trabajador-listar'),  # Solo lectura
    path('gestionar/', views.TrabajadorGestionarView.as_view(), name='trabajador-gestionar'),  # Gestionar
    path('crear/', views.TrabajadorCreateView.as_view(), name='trabajador-crear'),  # Crear
    path('editar/<int:pk>/', views.TrabajadorUpdateView.as_view(), name='trabajador-editar'),  # Editar
    path('eliminar/<int:pk>/', views.TrabajadorDeleteView.as_view(), name='trabajador-eliminar'),  # Confirmar eliminar
]