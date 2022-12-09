from django.db import models
from produccion.models import OrdenProduccion
from datetime import date, timedelta
 
today_date = date.today()
 
td = timedelta(8)

num_semana = today_date.isocalendar()
sem = num_semana[1]

fecha_anterior = today_date - td
fecha_posterior = today_date + td

Semana_ant = fecha_anterior.isocalendar()
Semana_post = fecha_posterior.isocalendar()

ant_sem = Semana_ant[1]
post_sem = Semana_post[1]

Semana =(
        (ant_sem, fecha_anterior),
        (sem, today_date),
        (post_sem, fecha_posterior),
    )

# Create your models here.
class Envios(models.Model):
    OProduct = models.ForeignKey(OrdenProduccion,verbose_name='Orden de Producción' ,related_name='OrdenProducto', on_delete=models.CASCADE)
    FechaPreparacion = models.CharField(choices=Semana, verbose_name='Semana de Produccion' ,max_length=250, help_text='La fecha puede ser este dia, una o dos semanas antes o una o dos semanas despues')
    CostoPlacas = models.SmallIntegerField(verbose_name='Costo Placas', null=True, blank=True)
    TotalPlacas = models.SmallIntegerField(verbose_name='Placas Totales', null=True, blank=True)
    FechaPlacas = models.DateField(auto_now=False, auto_now_add=False,verbose_name='Fecha de Preparación Placas', null=True, blank=True)
    FechaEnvioPlacas = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Envio Placas', null=True, blank=True)
    ReciboPlacas = models.BooleanField(verbose_name='Placas Recibidas', null=True, blank=True)
    Serigrafia = models.SmallIntegerField(verbose_name='Cantidad de Albanenes', null=True, blank=True)
    FechaSerigrafia = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Preparación Alabanenes', null=True, blank=True)
    FechaEnvioSeri = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Envio Albanene', null=True, blank=True)
    ReciboSerigrafia = models.BooleanField(verbose_name='Albanene Recibido', null=True, blank=True)
    CostoClisse = models.SmallIntegerField(verbose_name='Costo Clisse', null=True, blank=True)
    FechaClisse = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Preparación Clisse', null=True, blank=True)
    FechaEnvioClisse = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Envio Clisse', null=True, blank=True)
    ReciboClisse = models.BooleanField(verbose_name='Clisse Recibido', null=True, blank=True)
    CostoSuaje = models.SmallIntegerField(verbose_name='Costo Suaje', null=True, blank=True)
    FechaSuaje = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Preparación Suaje', null=True, blank=True)
    FechaEnvioSuaje = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Envio Suaje', null=True, blank=True)
    ReciboSuaje = models.BooleanField(verbose_name='Suaje Recibido', null=True, blank=True)
    CostoLaser = models.SmallIntegerField(verbose_name='Costo Laser', null=True, blank=True)
    FechaLaser = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Preparación Laser', null=True, blank=True)
    FechaEnvioLaser = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Envio Laser', null=True, blank=True)
    ReciboLaser = models.BooleanField(verbose_name='Corte Laser Recibido', null=True, blank=True)
    
    def __str__(self):
        return '{} • {}' .format(self.OProduct, self.FechaPreparacion)

    class Meta:
        db_table = 'SalidasProvedor'
        managed = True
        verbose_name = 'SalidasProvedor'
        verbose_name_plural = 'SalidasProvedores'