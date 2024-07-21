# tasks/views.py

from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Task
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def custom_logout(request):
    logout(request)
    return redirect('login') # Redirect to login page or wherever appropriate

def home(request):
    return render(request, 'home.html')

def taskcreate(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task =form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task-list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def profile(request):
    return render(request, 'profile.html')

# USer registration vieiw
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Create a form instance with POST data
        if form.is_valid(): # Check if the form is valid
            form.save() # Save the form data to create a new user
            return redirect('home') # Redirect to a success page
    else:
        form = UserCreationForm() # Create an empty form instance
    return render(request, 'tasks/register.html', {'form': form}) # Render the registration template with the form

# This view handles creating a new task
@login_required
def create_task(request):
    # If the request method is not POST, instantiate an empty form
    form = TaskForm()
    # Render the create_task.html template with the form
    return render(request, 'tasks/task_form.html', {'form': form})

# This view handles updating an existing task
@login_required
def update_task(request, task_id):
    # Get the task by its ID and ensure it belongs to the logged-in user
    task = get_object_or_404(Task, id=task_id)
    # Check if the request method is POST
    if request.method == 'POST':
        # Instantiate a TaskForm with the POST data and the task instanc
        form = TaskForm(request.POST, instance=task)
        # Validate the form
        if form.is_valid():
            # Save the changes to the task
            form.save()
            # Add a success message
            messages.success(request, 'Task updated successfull!y')
            # Redirect to the task list view
            return redirect('task_list')
    else:
        # If the request method is not POST, instantiate a form with the task instance
        form = TaskForm(instance=task)

    # Render the update_task.html template with the form
    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})

# update_url = reverse('update_task', args=[task.id])

# This view handles deleting an existing task
@login_required
def delete_task(request, task_id):
    # Get the task by its ID and ensure it belongs to the logged-in user
    task = get_object_or_404(Task, id=task_id)
    # Check if the request method is POST
    if request.method == 'POST':
        # Delete the task from the database
        task.delete()
        # Redirect to the task list view
        return redirect('task_list')

    # Render the delete_task.html template with the task
    return render(request, 'tasks/delete_task.html', {'task': task})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/home.html', {'form': form}) # Show error message

def user_logout(request):
    logout(request)
    return redirect('home') # Redirect to home page after logout

@login_required
def profile(request):
    return render(request, 'tasks/profile.html')

def home(request):
    return render(request, 'task/home.html') # Render the login page

# view to display the list of tasks
def task_list(request):
    tasks = Task.objects.all() # Retrieve all tasks from the database
    return render(request, 'tasks/task_list.html', {'tasks': tasks}) # Render the task list template with the tasks

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
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
