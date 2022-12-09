from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from bitacora.models import Envios

# Create your views here.
class EnvioListView(ListView):
    model = Envios
    context_object_name = 'EnvioList'
    template_name='envios/list.html'

class EnviosDetail(DetailView):
    model = Envios
    template_name='envios/detail.html'

class EnviosCreateView(CreateView):
    model = Envios
    template_name = "envios/create.html"
    fields = '__all__'
    success_url = reverse_lazy('envios:envios')

class EnviosUpdateView(UpdateView):
    model = Envios
    template_name = "envios/update.html"
    fields = '__all__'
    success_url = reverse_lazy('envios:envios')

class EnviosDeleteView(DeleteView):
    model = Envios
    template_name = "envios/delete.html"
    fields = '__all__'
    success_url = reverse_lazy('envios:envios')
