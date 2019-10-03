from django.urls import path
from . import views


app_name = 'bsapp'

urlpatterns = [
    path('', views.index, name='index'),
]
