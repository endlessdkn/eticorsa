from django.urls import path
from almacen.views import *

app_name = 'papel'

urlpatterns = [
    path('', PapelListView.as_view(), name='papel'),
    path('create/', PapelCreate.as_view(), name='papel_create'),
    path('<pk>/', PapelDetail.as_view(), name='papel_detail'),
    path('<pk>/update/', PapelUpdate.as_view(), name='papel_update'),
    path('<pk>/delete/', PapelDelete.as_view(), name='papel_delete'),
]