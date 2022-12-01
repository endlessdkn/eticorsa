from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pedidos.models import OPedido

# Create your views here.
class OPedidoListView(ListView):
    model = OPedido
    context_object_name = 'OPedidoList'
    template_name='pedidos/list.html'

class OPedidoDetail(DetailView):
    model = OPedido
    template_name='pedidos/detail.html'