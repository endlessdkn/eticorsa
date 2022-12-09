from django.urls import path
from produccion.views import *

app_name = 'produccion'

urlpatterns = [
    path('', ProduccionListVIew.as_view(), name='produccion'),
    path('create/', ProduccionCreateView.as_view(), name='produccion_create'),
    path('<pk>/', ProduccionDetail.as_view(), name='produccion_detail'),
    path('<pk>/update/', ProducccionUpdateView.as_view(), name='produccion_update'),
    path('<pk>/delete/', ModelDeleteView.as_view(), name='produccion_delete'),
    
]