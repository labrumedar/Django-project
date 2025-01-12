from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('general_statistics', views.general_statistics, name='general_statistics')
]
