from django.urls import path
from . import views

urlpatterns = [
    path('orden/listar/', views.OrdenListView.as_view(), name='orden-listar'),
    path('orden/crear/', views.OrdenCreateView.as_view(), name='orden-crear'),
    path('orden/editar/<int:pk>/', views.OrdenUpdateView.as_view(), name='orden-editar'),
    path('orden/eliminar/<int:pk>/', views.OrdenDeleteView.as_view(), name='orden-eliminar'),
]
