from django.urls import path
from . import views

urlpatterns = [
    path('reportes/total-pagar/', views.TotalPagarReporteView.as_view(), name='reporte-total-pagar'),
    path('reportes/horas-por-ot/', views.HorasPorOTReporteView.as_view(), name='reporte-horas-por-ot'),
    path('reportes/horas-por-trabajador/', views.HorasPorTrabajadorReporteView.as_view(), name='reporte-horas-por-trabajador'),
    path('reportes/pago-por-ot/', views.PagoPorOTReporteView.as_view(), name='reporte-pago-por-ot'),
]
