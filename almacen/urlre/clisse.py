from django.urls import path
from almacen.views import *

app_name = 'clisse'

urlpatterns = [
    path('', ClisseListView.as_view(), name='clisse'),
    path('create/', ClisseCreate.as_view(), name='clisse_create'),
    path('<pk>/', ClisseDetail.as_view(), name='clisse_detail'),
    path('<pk>/update/', ClisseUpdate.as_view(), name='clisse_update'),
    path('<pk>/delete/', ClisseDelete.as_view(), name='clisse_delete'),
]