from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrabajadorListView.as_view(), name='trabajador_list'),
]