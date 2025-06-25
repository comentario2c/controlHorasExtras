from django.db import models
from trabajadores.models import Trabajador
from ordenes.models import OrdenTrabajo

class HoraExtra(models.Model):
    ID_HoraExtra = models.AutoField(primary_key=True)
    ID_Trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='horas_extras')
    ID_OrdenTrabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='horas_extras')
    Fecha = models.DateField()
    HoraInicio = models.TimeField()
    HoraFin = models.TimeField()
    HorasTrabajadas = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    BonoEspecial = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    MontoCalculado = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'reportes_horaextra'
        ordering = ['-Fecha', '-ID_HoraExtra']

    def __str__(self):
        return f"{self.ID_Trabajador.Nombre} - {self.ID_OrdenTrabajo.Descripcion} ({self.Fecha})"
