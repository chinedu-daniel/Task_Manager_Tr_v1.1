from django.urls import path
from .views import ProfileView  # Replace with your actual views

urlpatterns = [
        path('', ProfileView.as_view(), name='profile_home'),  # Adjust the path and view name as necessary
]
