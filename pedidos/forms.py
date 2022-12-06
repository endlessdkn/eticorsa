from django import forms
from pedidos.models import OPedido

class OPedidoForm(forms.ModelForm):
    
    class Meta:
        model = OPedido
        fields = ['Cliente', 'RegEntrada', 'Muestra', 'FotoPedido', 'FechaPed','FechaElab', 'Indicaciones']