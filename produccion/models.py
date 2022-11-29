from django.db import models
from django.contrib.auth.models import User
from pedidos.models import OPedido
from cliente.models import perfil
from almacen.models import *

# Create your models here.
class OrdenProduccion(models.Model):
    Tipo_Trabajo =(
        ('Nuevo','Nuevo'),
        ('Resurtido','Resurtido'),
        ('Reposición','Reposición'),
    )
    Grosor =(
        ('Sencillo','Sencillo'),
        ('Empalamado','Empalamado'),
        ('Doble Vista','Doble Vista'),
    )
    Folio = models.CharField(verbose_name='Folio de Producción No', max_length=15)
    FolioCliente = models.CharField(verbose_name='Folio de Cliente', max_length=10)
    Cliente = models.ForeignKey(perfil, related_name='Cliente',verbose_name='Cliente', on_delete=models.CASCADE)
    NombreTrabajo = models.CharField(verbose_name='Nombre del Trabajo', max_length=250)
    FechaElaboracion = models.DateField(verbose_name='Fecha de Elaboración', auto_now=False, auto_now_add=False)
    TipoTrabajo = models.CharField(verbose_name='Tipo de Orde',choices=Tipo_Trabajo, max_length=15)
    ImpresionFrente = models.ManyToManyField(Tinta, verbose_name='Tintas Frente', related_name='ImpresionFrente', blank=True)
    ImpresionReverso = models.ManyToManyField(Tinta, verbose_name='Tintas Reverso', related_name='ImpresionReverso', blank=True)
    TipoGrosor = models.CharField(verbose_name='Tipo de Orde',choices=Grosor, max_length=15)
    TipoBarniz = models.ForeignKey(Barniz, verbose_name='Tipo de barniz', on_delete=models.CASCADE, related_name='TipoBarniz', null=True, blank=True)
    TipoLaminado = models.ForeignKey(Laminado, verbose_name='Tipo de Laminado', on_delete=models.CASCADE, related_name='TipoLaminado', null=True, blank=True)
    TipoClisse = models.ForeignKey(Clisse, verbose_name='Tipo de Clisse', on_delete=models.CASCADE, related_name='TipoClisse', null=True, blank=True)
    HotStamping = models.ForeignKey(Foil, verbose_name='Hot Stamping', on_delete=models.CASCADE, related_name='HotStamping', null=True, blank=True)
    TipoBotado = models.ForeignKey(Laser, verbose_name='Botado', on_delete=models.CASCADE, related_name='Botado', null=True, blank=True)
    TipoSuaje = models.ForeignKey(Suaje, verbose_name='Suaje', on_delete=models.CASCADE, related_name='Suaje')
    TipoPapel = models.ForeignKey(Papel, verbose_name='Papel', on_delete=models.CASCADE, related_name='Papel')
    CantidadPapel = models.SmallIntegerField(verbose_name='Tamaños Asignados')
    CantidadMerma = models.SmallIntegerField(verbose_name='Merma Asignada')
    OrdenPedido = models.ForeignKey(OPedido, verbose_name='Pedido Original', on_delete=models.CASCADE, related_name='Orden_Pedido')
    PedidoCantidad = models.PositiveIntegerField(verbose_name='Cantidad Solicitada')
    Observaciones = models.TextField(verbose_name='Observaciones', null=True, blank=True)
    ElaboradoPor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Elaborado Por:')

    def totalpapel(self):
        resultado = self.CantidadPapel + self.CantidadMerma
        return resultado

    def numgrosor(self):
        if (self.TipoGrosor == 'Empalamado'):
            return 2
        else:
            return 1
    
    def pzas_suaje(self):
        pzas = self.TipoSuaje.CantEtiqueta
        return pzas

    def __str__(self):
        return '{} • {}-{} - {} • {}' .format(self.Folio, self.FolioCliente, self.Cliente, self.NombreTrabajo, self.PedidoCantidad)

    class Meta:
        db_table = 'OrdenProduccion'
        managed = True
        verbose_name = 'OrdenProduccion'
        verbose_name_plural = 'OrdenProduccions'