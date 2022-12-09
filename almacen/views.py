from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from almacen.models import *

# Create your views here.
#Vista para clasificaicon de modelos de almacen
class ControlView(TemplateView):
    template_name = "almacen/control.html"

#Listas en almacen

class PapelListView(ListView):
    model = Papel
    context_object_name = 'PapelList'
    template_name='almacen/papel/list.html'

class TintaListView(ListView):
    model = Tinta
    context_object_name = 'TintaList'
    template_name='almacen/tinta/list.html'

class BarnizListView(ListView):
    model = Barniz
    context_object_name = 'BarnizList'
    template_name='almacen/barniz/list.html'

class SuajeListView(ListView):
    model = Suaje
    context_object_name = 'SuajeList'
    template_name='almacen/suaje/list.html'

class ClisseListView(ListView):
    model = Clisse
    context_object_name = 'ClisseList'
    template_name='almacen/clisse/list.html'

class LaserListView(ListView):
    model = Laser
    context_object_name = 'LaserList'
    template_name='almacen/laser/list.html'

class FoilListView(ListView):
    model = Foil
    context_object_name = 'FoilList'
    template_name='almacen/foil/list.html'

class FoilListView(ListView):
    model = Foil
    context_object_name = 'FoilList'
    template_name='almacen/foil/list.html'

class LaminadoListView(ListView):
    model = Laminado
    context_object_name = 'LaminadoList'
    template_name='almacen/laminado/list.html'

#Detalles de cada producto en almacen

class PapelDetail(DetailView):
    model = Papel
    template_name='almacen/papel/detail.html'

class TintaDetail(DetailView):
    model = Tinta
    template_name='almacen/tinta/detail.html'

class BarnizDetail(DetailView):
    model = Barniz
    template_name='almacen/barniz/detail.html'

class SuajeDetail(DetailView):
    model = Suaje
    template_name='almacen/suaje/detail.html'

class ClisseDetail(DetailView):
    model = Clisse
    template_name='almacen/clisse/detail.html'

class LaserDetail(DetailView):
    model = Laser
    template_name='almacen/laser/detail.html'

class FoilDetail(DetailView):
    model = Foil
    template_name='almacen/foil/detail.html'

class FoilDetail(DetailView):
    model = Foil
    template_name='almacen/foil/detail.html'

class LaminadoDetail(DetailView):
    model = Laminado
    template_name='almacen/laminado/detail.html'

# Vista de Creacion de Productos en almacen

class PapelCreate(CreateView):
    model = Papel
    template_name='almacen/papel/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class TintaCreate(CreateView):
    model = Tinta
    template_name='almacen/tinta/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class BarnizCreate(CreateView):
    model = Barniz
    template_name='almacen/barniz/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class SuajeCreate(CreateView):
    model = Suaje
    template_name='almacen/suaje/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class ClisseCreate(CreateView):
    model = Clisse
    template_name='almacen/clisse/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class LaserCreate(CreateView):
    model = Laser
    template_name='almacen/laser/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class FoilCreate(CreateView):
    model = Foil
    template_name='almacen/foil/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class FoilCreate(CreateView):
    model = Foil
    template_name='almacen/foil/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class LaminadoCreate(CreateView):
    model = Laminado
    template_name='almacen/laminado/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

#Clase para actualizar

class PapelUpdate(UpdateView):
    model = Papel
    template_name='almacen/papel/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class TintaUpdate(UpdateView):
    model = Tinta
    template_name='almacen/tinta/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class BarnizUpdate(UpdateView):
    model = Barniz
    template_name='almacen/barniz/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class SuajeUpdate(UpdateView):
    model = Suaje
    template_name='almacen/suaje/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class ClisseUpdate(UpdateView):
    model = Clisse
    template_name='almacen/clisse/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class LaserUpdate(UpdateView):
    model = Laser
    template_name='almacen/laser/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class FoilUpdate(UpdateView):
    model = Foil
    template_name='almacen/foil/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class FoilUpdate(UpdateView):
    model = Foil
    template_name='almacen/foil/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class LaminadoUpdate(UpdateView):
    model = Laminado
    template_name='almacen/laminado/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

#Vistas para Borrar

class PapelDelete(DeleteView):
    model = Papel
    template_name='almacen/papel/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class TintaDelete(DeleteView):
    model = Tinta
    template_name='almacen/tinta/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class BarnizDelete(DeleteView):
    model = Barniz
    template_name='almacen/barniz/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class SuajeDelete(DeleteView):
    model = Suaje
    template_name='almacen/suaje/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class ClisseDelete(DeleteView):
    model = Clisse
    template_name='almacen/clisse/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class LaserDelete(DeleteView):
    model = Laser
    template_name='almacen/laser/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class FoilDelete(DeleteView):
    model = Foil
    template_name='almacen/foil/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class FoilDelete(DeleteView):
    model = Foil
    template_name='almacen/foil/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')

class LaminadoDelete(DeleteView):
    model = Laminado
    template_name='almacen/laminado/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')