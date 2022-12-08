from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from pedidos.models import OPedido
#from pedidos.forms import OPedidoForm

# Create your views here.
class OPedidoListView(ListView):
    model = OPedido
    context_object_name = 'OPedidoList'
    template_name='pedidos/list.html'

class OPedidoDetail(DetailView):
    model = OPedido
    template_name='pedidos/detail.html'

class OPedidoCreateView(CreateView):
    model = OPedido
    #form_class = OPedidoForm
    fields = '__all__'
    template_name = "pedidos/create.html"
    success_url = reverse_lazy('pedidos:pedidos')

class OPedidoUpdateView(UpdateView):
    model = OPedido
    #form_class = OPedidoForm
    fields = '__all__'
    template_name = "pedidos/update.html"
    success_url = reverse_lazy('pedidos:pedidos')

class OPedidoDeleteView(DeleteView):
    model = OPedido
    #form_class = OPedidoForm
    fields = '__all__'
    template_name = "pedidos/delete.html"
    success_url = reverse_lazy('pedidos:pedidos')
