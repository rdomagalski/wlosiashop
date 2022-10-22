from django.urls import path

from . import views

urlpatterns = [
    path('sklep', views.index, name='index'),
]