# tasks/models.py

import uuid
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Model for representing a tasks
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255) # Title of the task
    description = models.TextField() # Description of the task
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp when the task was created
    updated_at = models.DateTimeField(auto_now=True) # Timestamp when the task was last updated
    priority = models.CharField(max_length=50) # Priority level of the task
    due_date = models.DateField() # Due date of the task
    completed = models.BooleanField(default=False) # Completion status of the task
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User who created the task

    def __str__(self):
        return self.name # string representation of the task
