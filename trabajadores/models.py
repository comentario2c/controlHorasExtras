from django.db import models

# Este modelo representa a un trabajador y sus datos relacionados con el cálculo de horas ordinarias y extras
# donde se manejan los datos con decimales intermanente y se redondean al guardar el objeto en la base de datos.
# cada vez que se utilice el método save() se recalculan los valores de total, hora_ordinaria y hora_extra.
# de esta manera se asegura que los cálculos sean precisos y se mantenga la integridad de los datos en la base de datos.
# finalmente se agrega el campo fecha_contrato para almacenar la fecha de inicio del contrato del trabajador.
# de esta manera se puede calcular la cantidad de días de vacaciones que le corresponden al trabajador
# y se puede llevar un control de la antigüedad del trabajador en la empresa.

class Trabajador(models.Model):
    ID_Trabajador = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=225, null=False, blank=False)
    fecha_contrato = models.DateField()
    monto_base = models.IntegerField(default=0)
    bono_produccion = models.IntegerField(default=0)
    hora_ordinaria = models.IntegerField(default=0)
    hora_extra = models.IntegerField(default=0)

    # Fórmula proporcionada por la empresa para calcular el valor de la hora ordinaria:
    # ((MontoBase + BonoProduccion) / 30) * 28) / 180
    # Se ajusta considerando 28 días trabajados al mes y 180 horas laborales mensuales.
    # Esta fórmula fue confirmada directamente con la administración para respetar su política interna.

    def calcular_hora_ordinaria(self):
        sueldo_mensual = self.monto_base + self.bono_produccion 
        return ((sueldo_mensual / 30) * 28) / 180

    def calcular_hora_extra(self):
        return self.calcular_hora_ordinaria() * 2

    def save(self, *args, **kwargs):
        self.hora_ordinaria = round(self.calcular_hora_ordinaria())
        self.hora_extra = round(self.calcular_hora_extra())
        super().save(*args, **kwargs)