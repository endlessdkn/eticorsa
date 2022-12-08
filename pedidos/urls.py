from django.urls import path
from pedidos.views import *

app_name = 'pedidos'

urlpatterns = [
    path('pedidos', OPedidoListView.as_view(), name='pedidos'),
    path('pedidos/create', OPedidoCreateView.as_view(), name='pedidos_create'),
    path('pedidos/<pk>', OPedidoDetail.as_view(), name='pedidos_detail'),
    path('pedidos/<pk>/update', OPedidoUpdateView.as_view(), name='pedidos_update'),
    path('pedidos/<pk>/delete', OPedidoDeleteView.as_view(), name='pedidos_delete'),
    
]