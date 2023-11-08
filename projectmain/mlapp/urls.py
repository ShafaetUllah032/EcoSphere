from django.urls import path
from . import views

urlpatterns = [
    path('mlapp/', views.mlapp, name='mlapp'),
]