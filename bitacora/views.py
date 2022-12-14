from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from bitacora.models import Envios
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
class EnvioListView(PermissionRequiredMixin, ListView):
    model = Envios
    context_object_name = 'EnvioList'
    template_name='envios/list.html'
    paginate_by = 9
    ordering = ['-id']
    permission_required = 'bitacora.view_envios'

class EnviosDetail(PermissionRequiredMixin, DetailView):
    model = Envios
    template_name='envios/detail.html'
    permission_required = 'bitacora.view_envios'

class EnviosCreateView(PermissionRequiredMixin, CreateView):
    model = Envios
    template_name = "envios/create.html"
    fields = '__all__'
    success_url = reverse_lazy('envios:envios')
    permission_required = ('bitacora.view_envios', 'bitacora.add_envios')

class EnviosUpdateView(PermissionRequiredMixin, UpdateView):
    model = Envios
    template_name = "envios/update.html"
    fields = '__all__'
    success_url = reverse_lazy('envios:envios')
    permission_required = ('bitacora.view_envios', 'bitacora.add_envios')

class EnviosDeleteView(PermissionRequiredMixin, DeleteView):
    model = Envios
    template_name = "envios/delete.html"
    fields = '__all__'
    success_url = reverse_lazy('envios:envios')
    permission_required = ('bitacora.view_envios', 'bitacora.delete_envios')
