from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from produccion.models import OrdenProduccion

# Create your views here.
class ProduccionListVIew(ListView):
    model = OrdenProduccion
    context_object_name = 'ProduccionList'
    template_name='produccion/list.html'

class ProduccionDetail(DetailView):
    model = OrdenProduccion
    template_name='produccion/detail.html'

class ProduccionCreateView(CreateView):
    model = OrdenProduccion
    template_name = "produccion/create.html"
    fields = '__all__'
    success_url = reverse_lazy('produccion:produccion')

class ProducccionUpdateView(UpdateView):
    model = OrdenProduccion
    template_name = "produccion/update.html"
    fields = '__all__'
    success_url = reverse_lazy('produccion:produccion')

class ModelDeleteView(DeleteView):
    model = OrdenProduccion
    template_name = "produccion/delete.html"
    fields = '__all__'
    success_url = reverse_lazy('produccion:produccion')
