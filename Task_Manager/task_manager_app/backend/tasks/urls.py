# tasks/urls.py

from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from task_manager.views import home  # Adjust the import path as necessary
from .views import (
        TaskListView,
        TaskCreateView,
        TaskUpdateView,
        TaskDeleteView,
)

urlpatterns = [
        path('admin/', admin.site.urls),
        #path('', home, name='home'),# URL for the home page
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout,html'), name='logout'),
        path('profile/', views.profile, name='profile'),
        path('register/', views.register, name='profile'),
        path('accounts/', include('django.contrib.auth.urls')),
        path('', views.task_list, name='task-list'),
        path('create/', views.taskcreate, name='task-create'),
        path('tasks/<int:task_id>/update/', views.task_update, name='update_task'),
        path('<int:task_id>/delete/', views.task_delete, name='delete_task'),
]
