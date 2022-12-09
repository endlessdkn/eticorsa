from django.urls import path
from almacen.views import *

app_name = 'barniz'

urlpatterns = [
    path('', BarnizListView.as_view(), name='barniz'),
    path('create/', BarnizCreate.as_view(), name='barniz_create'),
    path('<pk>/', BarnizDetail.as_view(), name='barniz_detail'),
    path('<pk>/update/', BarnizUpdate.as_view(), name='barniz_update'),
    path('<pk>/delete/', BarnizDelete.as_view(), name='barniz_delete'),
]