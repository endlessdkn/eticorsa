from django.urls import path
from empresa import views

app_name = 'empresa'

urlpatterns = [
    path('', views.index, name='index'),
]