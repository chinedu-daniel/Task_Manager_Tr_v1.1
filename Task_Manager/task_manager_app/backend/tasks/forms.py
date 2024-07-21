# forms.py

from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True) # Add an email field to the registration form
    class Meta:
        model = User # Use the User model
        fields = ['username', 'email', 'password1', 'password2'] # Fields to include in the form

# Form for creating and updating tasks
class TaskForm(forms.ModelForm):
    class Meta:
        # Specify the model to usd
        model = Task
        # Define the fields to include in the form
        fields = ['name', 'description', 'due_date', 'completed']
