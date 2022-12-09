from django.urls import path
from almacen.views import *

app_name = 'tinta'

urlpatterns = [
    path('', TintaListView.as_view(), name='tinta'),
    path('create/', TintaCreate.as_view(), name='tinta_create'),
    path('<pk>/', TintaDetail.as_view(), name='tinta_detail'),
    path('<pk>/update/', TintaUpdate.as_view(), name='tinta_update'),
    path('<pk>/delete/', TintaDelete.as_view(), name='tinta_delete'),
]