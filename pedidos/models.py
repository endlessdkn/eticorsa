from django.db import models
from cliente.models import perfil

# Create your models here.
class OPedido(models.Model):
    Muestra=(
            ('Fisica','Fisica'),
            ('Digital','Digital'),
            ('Domi','Domi'),
            ('Fotografica','Fotografica')
    )
    Cliente = models.ForeignKey(perfil, verbose_name='Cliente', related_name='Cliente_OP', on_delete=models.CASCADE)
    RegEntrada = models.CharField(verbose_name='Nombre del Pedido', max_length=150)
    Muestra = models.CharField(verbose_name='Tipo de Muestra', choices=Muestra, max_length=150)
    FotoPedido = models.ImageField(verbose_name='Imagen del Pedido', upload_to='static/pedidos/', height_field=None, width_field=None, max_length=None)
    FechaPed = models.DateField(verbose_name='Fecha del Pedido', auto_now=False, auto_now_add=False)
    FechaElab = models.DateField(verbose_name='Fecha del Recepcion', auto_now=False, auto_now_add=False)
    Indicaciones = models.TextField(verbose_name='Indicaciones',null=True, blank=True, help_text='Aqui van algunas opservaciones especiales dentro del pedido')

    def __str__(self):
        return self.RegEntrada

    class Meta:
        db_table = 'OPedidos'
        managed = True
        verbose_name = 'OPedido'
        verbose_name_plural = 'OPedidos'