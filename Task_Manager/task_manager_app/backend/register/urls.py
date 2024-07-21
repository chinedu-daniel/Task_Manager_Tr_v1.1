# register/urls.py

from django.urls import path
from . import views

urlpatterns = [
        path('', views.register, name='register'),  # Replace 'register' with your actual view
]

