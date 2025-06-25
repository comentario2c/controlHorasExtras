from django.views.generic import TemplateView
from django.db.models import Sum
from trabajadores.models import Trabajador
# from ordenes.models import OrdenTrabajo
from horas_extras.models import HoraExtra

class TotalPagarReporteView(TemplateView):
    template_name = "reportes/total_pagar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener suma de horas extras, bonos y monto calculado por trabajador
        data = HoraExtra.objects.values(
            'ID_Trabajador',
            'ID_Trabajador__Nombre'
        ).annotate(
            total_horas_extra=Sum('HorasTrabajadas'),
            total_bonos=Sum('BonoEspecial'),
            total_pagar=Sum('MontoCalculado'),
        ).order_by('ID_Trabajador__Nombre')

        context['reporte'] = data
        return context

class HorasPorOTReporteView(TemplateView):
    template_name = "reportes/horas_por_ot.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Suma horas trabajadas agrupadas por orden de trabajo
        ot_data = HoraExtra.objects.values(
            'ID_OrdenTrabajo',
            'ID_OrdenTrabajo__Descripcion'
        ).annotate(
            total_horas=Sum('HorasTrabajadas')
        ).order_by('ID_OrdenTrabajo__Descripcion')

        context['reporte'] = ot_data
        return context

class HorasPorTrabajadorReporteView(TemplateView):
    template_name = "reportes/horas_por_trabajador.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []

        for trabajador in Trabajador.objects.all():
            total_horas = trabajador.horas_extras.aggregate(
                total=Sum('HorasTrabajadas')
            )['total'] or 0

            data.append({
                'trabajador': trabajador,
                'total_horas': total_horas,
            })

        context['reporte'] = data
        return context


class PagoPorOTReporteView(TemplateView):
    template_name = "reportes/pago_por_ot.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Suma monto a pagar por trabajador y orden de trabajo
        pagos_data = HoraExtra.objects.values(
            'ID_Trabajador',
            'ID_Trabajador__Nombre',
            'ID_OrdenTrabajo',
            'ID_OrdenTrabajo__Descripcion'
        ).annotate(
            total_pago=Sum('MontoCalculado')
        ).order_by('ID_Trabajador__Nombre', 'ID_OrdenTrabajo__Descripcion')

        context['reporte'] = pagos_data
        return context
