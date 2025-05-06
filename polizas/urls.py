from django.urls import path
from . import views

urlpatterns = [
    path('', views.polizas, name='polizas'),
]