from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from almacen.models import *
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

# Create your views here.
#Vista para clasificaicon de modelos de almacen
class ControlView(LoginRequiredMixin, TemplateView):
    template_name = "almacen/control.html"

#Listas en almacen
class PapelListView(PermissionRequiredMixin, ListView):
    model = Papel
    context_object_name = 'PapelList'
    template_name='almacen/papel/list.html'
    paginate_by = 9
    ordering = ['-id']
    permission_required = 'almacen.view_modelo'

class TintaListView(PermissionRequiredMixin, ListView):
    model = Tinta
    context_object_name = 'TintaList'
    template_name='almacen/tinta/list.html'
    paginate_by = 9
    ordering = ['-id']
    permission_required = 'almacen.view_modelo'

class BarnizListView(PermissionRequiredMixin, ListView):
    model = Barniz
    context_object_name = 'BarnizList'
    template_name='almacen/barniz/list.html'
    paginate_by = 9
    ordering = ['-id']
    permission_required = 'almacen.view_modelo'

class SuajeListView(PermissionRequiredMixin, ListView):
    model = Suaje
    context_object_name = 'SuajeList'
    template_name='almacen/suaje/list.html'
    paginate_by = 9
    ordering = ['-id']
    permission_required = 'almacen.view_modelo'

class ClisseListView(PermissionRequiredMixin, ListView):
    model = Clisse
    context_object_name = 'ClisseList'
    template_name='almacen/clisse/list.html'
    paginate_by = 9
    ordering = ['-id']
    permission_required = 'almacen.view_modelo'

class LaserListView(PermissionRequiredMixin, ListView):
    model = Laser
    context_object_name = 'LaserList'
    template_name='almacen/laser/list.html'
    paginate_by = 9
    ordering = ['-id']
    permission_required = 'almacen.view_modelo'

class FoilListView(PermissionRequiredMixin, ListView):
    model = Foil
    context_object_name = 'FoilList'
    template_name='almacen/foil/list.html'
    paginate_by = 9
    ordering = ['-id']
    permission_required = 'almacen.view_modelo'

class LaminadoListView(PermissionRequiredMixin, ListView):
    model = Laminado
    context_object_name = 'LaminadoList'
    template_name='almacen/laminado/list.html'
    paginate_by = 9
    ordering = ['-id']
    permission_required = 'almacen.view_modelo'

#Detalles de cada producto en almacen

class PapelDetail(PermissionRequiredMixin, DetailView):
    model = Papel
    template_name='almacen/papel/detail.html'
    permission_required = 'almacen.view_modelo'

class TintaDetail(PermissionRequiredMixin, DetailView):
    model = Tinta
    template_name='almacen/tinta/detail.html'
    permission_required = 'almacen.view_modelo'

class BarnizDetail(PermissionRequiredMixin, DetailView):
    model = Barniz
    template_name='almacen/barniz/detail.html'
    permission_required = 'almacen.view_modelo'

class SuajeDetail(PermissionRequiredMixin, DetailView):
    model = Suaje
    template_name='almacen/suaje/detail.html'
    permission_required = 'almacen.view_modelo'

class ClisseDetail(PermissionRequiredMixin, DetailView):
    model = Clisse
    template_name='almacen/clisse/detail.html'
    permission_required = 'almacen.view_modelo'

class LaserDetail(PermissionRequiredMixin, DetailView):
    model = Laser
    template_name='almacen/laser/detail.html'
    permission_required = 'almacen.view_modelo'

class FoilDetail(PermissionRequiredMixin, DetailView):
    model = Foil
    template_name='almacen/foil/detail.html'
    permission_required = 'almacen.view_modelo'

class LaminadoDetail(PermissionRequiredMixin, DetailView):
    model = Laminado
    template_name='almacen/laminado/detail.html'
    permission_required = 'almacen.view_modelo'

# Vista de Creacion de Productos en almacen

class PapelCreate(PermissionRequiredMixin, CreateView):
    model = Papel
    template_name='almacen/papel/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class TintaCreate(PermissionRequiredMixin, CreateView):
    model = Tinta
    template_name='almacen/tinta/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class BarnizCreate(PermissionRequiredMixin, CreateView):
    model = Barniz
    template_name='almacen/barniz/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class SuajeCreate(PermissionRequiredMixin, CreateView):
    model = Suaje
    template_name='almacen/suaje/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class ClisseCreate(PermissionRequiredMixin, CreateView):
    model = Clisse
    template_name='almacen/clisse/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class LaserCreate(PermissionRequiredMixin, CreateView):
    model = Laser
    template_name='almacen/laser/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class FoilCreate(PermissionRequiredMixin, CreateView):
    model = Foil
    template_name='almacen/foil/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class LaminadoCreate(PermissionRequiredMixin, CreateView):
    model = Laminado
    template_name='almacen/laminado/create.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

#Clase para actualizar

class PapelUpdate(PermissionRequiredMixin, UpdateView):
    model = Papel
    template_name='almacen/papel/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class TintaUpdate(PermissionRequiredMixin, UpdateView):
    model = Tinta
    template_name='almacen/tinta/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class BarnizUpdate(PermissionRequiredMixin, UpdateView):
    model = Barniz
    template_name='almacen/barniz/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class SuajeUpdate(PermissionRequiredMixin, UpdateView):
    model = Suaje
    template_name='almacen/suaje/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class ClisseUpdate(PermissionRequiredMixin, UpdateView):
    model = Clisse
    template_name='almacen/clisse/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class LaserUpdate(PermissionRequiredMixin, UpdateView):
    model = Laser
    template_name='almacen/laser/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class FoilUpdate(PermissionRequiredMixin, UpdateView):
    model = Foil
    template_name='almacen/foil/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

class LaminadoUpdate(PermissionRequiredMixin, UpdateView):
    model = Laminado
    template_name='almacen/laminado/update.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.add_modelo')

#Vistas para Borrar

class PapelDelete(PermissionRequiredMixin, DeleteView):
    model = Papel
    template_name='almacen/papel/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.delete_modelo')

class TintaDelete(PermissionRequiredMixin, DeleteView):
    model = Tinta
    template_name='almacen/tinta/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.delete_modelo')

class BarnizDelete(PermissionRequiredMixin, DeleteView):
    model = Barniz
    template_name='almacen/barniz/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.delete_modelo')

class SuajeDelete(PermissionRequiredMixin, DeleteView):
    model = Suaje
    template_name='almacen/suaje/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.delete_modelo')

class ClisseDelete(PermissionRequiredMixin, DeleteView):
    model = Clisse
    template_name='almacen/clisse/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.delete_modelo')

class LaserDelete(PermissionRequiredMixin, DeleteView):
    model = Laser
    template_name='almacen/laser/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.delete_modelo')

class FoilDelete(PermissionRequiredMixin, DeleteView):
    model = Foil
    template_name='almacen/foil/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.delete_modelo')

class LaminadoDelete(PermissionRequiredMixin, DeleteView):
    model = Laminado
    template_name='almacen/laminado/delete.html'
    fields = '__all__'
    success_url = reverse_lazy('almacen:almacen')
    permission_required = ('almacen.view_modelo','almacen.delete_modelo')