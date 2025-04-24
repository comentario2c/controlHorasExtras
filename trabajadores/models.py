from django.db import models

# Este modelo representa a un trabajador y sus datos relacionados con el cálculo de horas ordinarias y extras
# donde se manejan los datos con decimales intermanente y se redondean al guardar el objeto en la base de datos.
# cada vez que se utilice el método save() se recalculan los valores de total, hora_ordinaria y hora_extra.
# de esta manera se asegura que los cálculos sean precisos y se mantenga la integridad de los datos en la base de datos.

class Trabajador(models.Model):
    ID_Trabajador = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=225, null=False, blank=False)
    monto_base = models.IntegerField(default=0)
    bono_produccion = models.IntegerField(default=0)
    hora_ordinaria = models.IntegerField(default=0)
    hora_extra = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def calcular_hora_ordinaria(self):
        return ((self.total / 30) * 28) / 180 if self.total else 0

    def calcular_hora_extra(self):
        return self.calcular_hora_ordinaria() * 2

    def save(self, *args, **kwargs):
        self.total = self.monto_base + self.bono_produccion
        self.hora_ordinaria = round(self.calcular_hora_ordinaria())
        self.hora_extra = round(self.calcular_hora_extra())
        super().save(*args, **kwargs)