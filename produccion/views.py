from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from produccion.models import OrdenProduccion
from django.contrib.auth.mixins import PermissionRequiredMixin
from empresa.models import Empresa


# Create your views here.
class ProduccionListVIew(PermissionRequiredMixin, ListView):
    model = OrdenProduccion
    context_object_name = 'ProduccionList'
    template_name='produccion/list.html'
    paginate_by = 9
    ordering = ['-id']
    permission_required = 'produccion.view_ordenproduccion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.all()
        return context

class ProduccionDetail(PermissionRequiredMixin, DetailView):
    model = OrdenProduccion
    template_name='produccion/detail.html'
    permission_required = 'produccion.view_ordenproduccion'

class ProduccionCreateView(PermissionRequiredMixin, CreateView):
    model = OrdenProduccion
    template_name = "produccion/create.html"
    fields = '__all__'
    success_url = reverse_lazy('produccion:produccion')
    permission_required = ('produccion.view_ordenproduccion', 'produccion.add_ordenproduccion')

class ProducccionUpdateView(PermissionRequiredMixin, UpdateView):
    model = OrdenProduccion
    template_name = "produccion/update.html"
    fields = '__all__'
    success_url = reverse_lazy('produccion:produccion')
    permission_required = ('produccion.view_ordenproduccion', 'produccion.add_ordenproduccion')

class ModelDeleteView(PermissionRequiredMixin, DeleteView):
    model = OrdenProduccion
    template_name = "produccion/delete.html"
    fields = '__all__'
    success_url = reverse_lazy('produccion:produccion')
    permission_required = ('produccion.view_ordenproduccion', 'produccion.delete_ordenproduccion')
