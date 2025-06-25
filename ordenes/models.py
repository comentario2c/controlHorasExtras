from django.db import models

# Create your models here.
class OrdenTrabajo(models.Model):
    ID_OrdenTrabajo = models.IntegerField(primary_key=True)
    Descripcion = models.CharField(max_length=255, null=False, blank=False)
