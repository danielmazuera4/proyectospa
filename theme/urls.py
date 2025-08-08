from django.urls import path
from .views import principal  # Asegúrate de que esta vista exista en views.py

urlpatterns = [
    path('', principal, name='principal'),
]
