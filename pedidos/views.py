from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from pedidos.models import OPedido
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
class OPedidoListView(PermissionRequiredMixin, ListView):
    model = OPedido
    context_object_name = 'OPedidoList'
    template_name='pedidos/list.html'
    paginate_by = 9
    permission_required = 'pedidos.view_opedido'
    ordering = ['-id']

class OPedidoDetail(PermissionRequiredMixin, DetailView):
    model = OPedido
    template_name='pedidos/detail.html'
    permission_required = 'pedidos.view_opedido'

class OPedidoCreateView(PermissionRequiredMixin, CreateView):
    model = OPedido
    fields = '__all__'
    template_name = "pedidos/create.html"
    success_url = reverse_lazy('pedidos:pedidos')
    permission_required = ('pedidos.view_opedido', 'pedidos.add_opedido')

class OPedidoUpdateView(PermissionRequiredMixin, UpdateView):
    model = OPedido
    fields = '__all__'
    template_name = "pedidos/update.html"
    success_url = reverse_lazy('pedidos:pedidos')
    permission_required = ('pedidos.view_opedido', 'pedidos.add_opedido')

class OPedidoDeleteView(PermissionRequiredMixin, DeleteView):
    model = OPedido
    fields = '__all__'
    template_name = "pedidos/delete.html"
    success_url = reverse_lazy('pedidos:pedidos')
    permission_required = ('pedidos.view_opedido', 'pedidos.delete_opedido')