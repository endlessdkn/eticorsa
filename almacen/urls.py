from django.urls import path, include
from almacen.views import *

app_name = 'almacen'

#Agregar Laser
urlpatterns = [
    #Control
    path('', ControlView.as_view(), name='almacen'),
    #Listas
    path('barniz/', BarnizListView.as_view(), name='barniz'),
    path('clisse/', ClisseListView.as_view(), name='clisse'),
    path('foil/', FoilListView.as_view(), name='foil'),
    path('laminado/', LaminadoListView.as_view(), name='laminado'),
    path('suaje/', SuajeListView.as_view(), name='suaje'),
    path('tinta/', TintaListView.as_view(), name='tinta'),
    path('papel/', PapelListView.as_view(), name='papel'),
    path('laser/', LaserListView.as_view(), name='laser'),
    #Nuevos
    path('barniz/create/', BarnizCreate.as_view(), name='barniz_create'),
    path('clisse/create/', ClisseCreate.as_view(), name='clisse_create'),
    path('foil/create/', FoilCreate.as_view(), name='foil_create'),
    path('laminado/create/', LaminadoCreate.as_view(), name='laminado_create'),
    path('suaje/create/', SuajeCreate.as_view(), name='suaje_create'),
    path('tinta/create/', TintaCreate.as_view(), name='tinta_create'),
    path('papel/create/', PapelCreate.as_view(), name='papel_create'),
    path('laser/create/', LaserCreate.as_view(), name='laser_create'),
    #Detalle
    path('barniz/<pk>/', BarnizDetail.as_view(), name='barniz_detail'),
    path('clisse/<pk>/', ClisseDetail.as_view(), name='clisse_detail'),
    path('foil/<pk>/', FoilDetail.as_view(), name='foil_detail'),
    path('laminado/<pk>/', LaminadoDetail.as_view(), name='laminado_detail'),
    path('suaje/<pk>/', SuajeDetail.as_view(), name='suaje_detail'),
    path('tinta/<pk>/', TintaDetail.as_view(), name='tinta_detail'),
    path('papel/<pk>/', PapelDetail.as_view(), name='papel_detail'),
    path('laser/<pk>/', PapelDetail.as_view(), name='laser_detail'),
    #Modificacion
    path('barniz/<pk>/update/', BarnizUpdate.as_view(), name='barniz_update'),
    path('clisse/<pk>/update/', ClisseUpdate.as_view(), name='clisse_update'),
    path('foil/<pk>/update/', FoilUpdate.as_view(), name='foil_update'),
    path('laminado/<pk>/update/', LaminadoUpdate.as_view(), name='laminado_update'),
    path('suaje/<pk>/update/', SuajeUpdate.as_view(), name='suaje_update'),
    path('tinta/<pk>/update/', TintaUpdate.as_view(), name='tinta_update'),
    path('papel/<pk>/update/', PapelUpdate.as_view(), name='papel_update'),
    path('laser/<pk>/update/', LaserUpdate.as_view(), name='laser_update'),
    #Eliminacion
    path('barniz/<pk>/delete/', BarnizDelete.as_view(), name='barniz_delete'),
    path('clisse/<pk>/delete/', ClisseDelete.as_view(), name='clisse_delete'),
    path('foil/<pk>/delete/', FoilDelete.as_view(), name='foil_delete'),
    path('laminado/<pk>/delete/', LaminadoDelete.as_view(), name='laminado_delete'),
    path('suaje/<pk>/delete/', SuajeDelete.as_view(), name='suaje_delete'),
    path('tinta/<pk>/delete/', TintaDelete.as_view(), name='tinta_delete'),
    path('papel/<pk>/delete/', PapelDelete.as_view(), name='papel_delete'),
    path('laser/<pk>/delete/', LaserDelete.as_view(), name='laser_delete'),
]