from django.urls import path
from almacen.views import *

app_name = 'foil'

urlpatterns = [
    path('', FoilListView.as_view(), name='foil'),
    path('create/', FoilCreate.as_view(), name='foil_create'),
    path('<pk>/', FoilDetail.as_view(), name='foil_detail'),
    path('<pk>/update/', FoilUpdate.as_view(), name='foil_update'),
    path('<pk>/delete/', FoilDelete.as_view(), name='foil_delete'),
]