from django.urls import path, include
from . import views

urlpatterns = [
    path('inicio/', views.pagina_inicio, name='pagina_inicio'),
    path('trabajadores/', include('trabajadores.urls')), 
]