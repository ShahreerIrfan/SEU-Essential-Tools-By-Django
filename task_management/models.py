from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Category(models.Model):
    """Only admin users can create categories."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Subtask(models.Model):
    """Model for subtasks under a main task."""
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
        ('C', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('IP', 'In Progress'),
        ('D', 'Done'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(help_text="Deadline for the task")
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='P')
    is_recurring = models.BooleanField(default=False, help_text="Does the task repeat?")
    recurring_frequency = models.CharField(max_length=20, blank=True, null=True, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ])
    time_estimate = models.DurationField(help_text="Estimated time to complete the task", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    dependencies = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='dependent_tasks')
    completion_percentage = models.IntegerField(default=0)
    tags = models.CharField(max_length=100, blank=True, null=True, help_text="Comma-separated tags for filtering tasks")
    attachments = models.FileField(upload_to='task_files/', blank=True, null=True)
    notify_before = models.DurationField(default=timedelta(hours=1), help_text="Notify user before this time")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"

    @property
    def is_overdue(self):
        """Check if the task is overdue."""
        return self.due_date < timezone.now() and self.status != 'D'

    def auto_adjust_priority(self):
        """Automatically increase priority as the due date approaches."""
        time_left = self.due_date - timezone.now()
        if time_left < timedelta(days=1) and self.priority != 'C':
            self.priority = 'C'
        elif time_left < timedelta(days=3) and self.priority == 'M':
            self.priority = 'H'
        self.save()

    class Meta:
        ordering = ['due_date', 'priority']
