# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
        path('', views.login_view, name='login'),  # Replace 'login_view' with your actual view
]
