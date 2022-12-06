from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, reverse
from pedidos.models import OPedido
from pedidos.forms import OPedidoForm

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
    form_class = OPedidoForm
    template_name = "pedidos/create.html"

    def get_success_url(self):
        return reverse('pedidos')
