from django.urls import path, include
from almacen.views import ControlView
import almacen.urlre

app_name = 'almacen'

urlpatterns = [
    path('', ControlView.as_view(), name='almacen'),
    path('papel/', include('urlre.papel')),
    path('tinta/', include('urlre.tinta')),
    path('barniz/', include('urlre.barniz')),
    path('suaje/', include('urlre.suaje')),
    path('clisse/', include('urlre.clisse')),
    path('foil/', include('urlre.foil')),
    path('laminado/', include('urlre.laminado')),
]