# tasks/urls.py

from django.urls import path, include
from . import views
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.auth import views as auth_views
from task_manager.views import home  # Adjust the import path as necessary
from uuid import UUID
from .views import (
        TaskListView,
        TaskCreateView,
        TaskUpdateView,
        TaskDeleteView,
)

urlpatterns = [
        path('', views.home, name='home'),
        #path('some-view/', views.some_view, name='some-view'),
        path('admin/', admin.site.urls),
        #path('', home, name='home'),# URL for the home page
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout,html'), name='logout'),
        path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
        path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
        path('tasks/', TaskListView.as_view(), name='task_list'),
        #path('', RedirectView.as_view(url='/tasks/')),
        path('profile/', views.profile, name='profile'),
        path('register/', views.register, name='register'),
        path('accounts/', include('django.contrib.auth.urls')),
        path('list', views.task_list, name='task-list'),
        path('create/', views.task_create, name='task-create'),
        path('task/<uuid:pk>/update/', views.task_update, name='update_task'),
        path('task/<uuid:pk>/delete/', views.task_delete, name='delete_task'),
]
