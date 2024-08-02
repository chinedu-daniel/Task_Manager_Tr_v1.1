# tasks/views.py

from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm, UserRegisterForm, ProjectForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Task, Project
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

@login_required
def custom_logout(request):
    logout(request)
    return redirect('login') # Redirect to login page or wherever appropriate

@login_required
def home(request):
    return render(request, 'task/home.html')

@login_required
def some_view(request):
    return render(request, 'template_name.html')

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task =form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'task/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/task_update.html', {'task': task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task-list')
    return render(request, 'task/task_confirm_delete.html', {'task': task})

@login_required
def profile(request):
    return render(request, 'profile.html')

# USer registration view
@login_required
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Create a form instance with POST data
        if form.is_valid(): # Check if the form is valid
            form.save() # Save the form data to create a new user
            return redirect('home') # Redirect to a success page
    else:
        form = UserCreationForm() # Create an empty form instance
    return render(request, 'task/register.html', {'form': form}) # Render the registration template with the form

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'task/home.html', {'form': form}) # Show error message

def user_logout(request):
    logout(request)
    return redirect('home') # Redirect to home page after logout

@login_required
def profile(request):
    return render(request, 'task/profile.html')

def home(request):
    return render(request, 'task/home.html') # Render the login page

# view to display the list of tasks
def task_list(request):
    tasks = Task.objects.all() # Retrieve all tasks from the database
    return render(request, 'task/task_list.html') # Render the task list template with the tasks

class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('task-list')

    def get_object(self):
        task_id = self.kwargs.get("task_id")
        return Task.objects.get(id=task_id)

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

# Create your views here.
