from django.urls import path
from pedidos.views import *

app_name = 'pedidos'

urlpatterns = [
    path('pedidos', OPedidoListView.as_view(), name='pedidos'),
    path('pedidos/<pk>', OPedidoDetail.as_view(), name='pedidos_detail'),
]