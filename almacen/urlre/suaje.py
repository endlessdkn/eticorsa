from django.urls import path
from almacen.views import *

app_name = 'suaje'

urlpatterns = [
    path('', SuajeListView.as_view(), name='suaje'),
    path('create/', SuajeCreate.as_view(), name='suaje_create'),
    path('<pk>/', SuajeDetail.as_view(), name='suaje_detail'),
    path('<pk>/update/', SuajeUpdate.as_view(), name='suaje_update'),
    path('<pk>/delete/', SuajeDelete.as_view(), name='suaje_delete'),
]