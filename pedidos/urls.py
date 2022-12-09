from django.urls import path
from pedidos.views import *

app_name = 'pedidos'

urlpatterns = [
    path('', OPedidoListView.as_view(), name='pedidos'),
    path('create/', OPedidoCreateView.as_view(), name='pedidos_create'),
    path('<pk>/', OPedidoDetail.as_view(), name='pedidos_detail'),
    path('<pk>/update/', OPedidoUpdateView.as_view(), name='pedidos_update'),
    path('<pk>/delete/', OPedidoDeleteView.as_view(), name='pedidos_delete'),
    
]