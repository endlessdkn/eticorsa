from django.urls import path
from almacen.views import *

app_name = 'laminado'

urlpatterns = [
    path('', LaminadoListView.as_view(), name='laminado'),
    path('create/', LaminadoCreate.as_view(), name='laminado_create'),
    path('<pk>/', LaminadoDetail.as_view(), name='laminado_detail'),
    path('<pk>/update/', LaminadoUpdate.as_view(), name='laminado_update'),
    path('<pk>/delete/', LaminadoDelete.as_view(), name='laminado_delete'),
]