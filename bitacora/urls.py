from django.urls import path
from bitacora.views import *

app_name = 'envios'

urlpatterns = [
    path('', EnvioListView.as_view(), name='envios'),
    path('create/', EnviosCreateView.as_view(), name='envios_create'),
    path('<pk>/', EnviosDetail.as_view(), name='envios_detail'),
    path('<pk>/update/', EnviosUpdateView.as_view(), name='envios_update'),
    path('<pk>/delete/', EnviosDeleteView.as_view(), name='envios_delete'),
]