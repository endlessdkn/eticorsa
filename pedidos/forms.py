from django import forms
from pedidos.models import OPedido
from cliente.models import perfil

class pedidosForm(forms.ModelForm):
    Cliente = forms.ModelChoiceField(perfil, verbose_name='Cliente', related_name='Cliente_OP')
    RegEntrada = forms.CharField(verbose_name='Nombre del Pedido', max_length=150)
    Muestra = forms.CharField(verbose_name='Tipo de Muestra', choices=OPedido.Muestra, max_length=150)
    FotoPedido = forms.ImageField(verbose_name='Imagen del Pedido', upload_to='static/pedidos/', height_field=None, width_field=None, max_length=None)
    FechaPed = forms.DateField(verbose_name='Fecha del Pedido', auto_now=False, auto_now_add=False)
    FechaElab = forms.DateField(verbose_name='Fecha del Recepcion', auto_now=False, auto_now_add=False)
    Indicaciones = forms.CharField(verbose_name='Indicaciones',null=True, blank=True, help_text='Aqui van algunas opservaciones especiales dentro del pedido')
    
    class Meta:
        model = OPedido
        fields = ("",)
