from django.db import models
from produccion.models import OrdenProduccion

# Create your models here.
class SalidaMaterial(models.Model):
    OProduccion = models.ForeignKey(OrdenProduccion, on_delete=models.CASCADE, verbose_name='Orde de Produccion')
    Paquete1 = models.IntegerField(verbose_name='Paquete 1')
    Paquete2 = models.IntegerField(verbose_name='Paquete 2', null=True, blank=True)
    Paquete3 = models.IntegerField(verbose_name='Paquete 3', null=True, blank=True)
    Paquete4 = models.IntegerField(verbose_name='Paquete 4', null=True, blank=True)
    Paquete5 = models.IntegerField(verbose_name='Paquete 5', null=True, blank=True)
    Paquete6 = models.IntegerField(verbose_name='Paquete 6', null=True, blank=True)
    Paquete7 = models.IntegerField(verbose_name='Paquete 7', null=True, blank=True)
    Paquete8 = models.IntegerField(verbose_name='Paquete 8', null=True, blank=True)
    
    def totalPzas(self):
        total = self.Paquete1 + self.Paquete2 + self.Paquete3 + self.Paquete4 + self.Paquete5 + self.Paquete6 + self.Paquete7 + self.Paquete8
        return total

    def __str__(self):
        return '{} - {} pzas' .format (self.OProduccion, self.totalPzas)

    class Meta:
        db_table = 'SalidaMaterial'
        managed = True
        verbose_name = 'SalidaMaterial'
        verbose_name_plural = 'SalidaMateriales'