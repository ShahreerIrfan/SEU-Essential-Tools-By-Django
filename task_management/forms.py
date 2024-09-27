from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 
            'description', 
            'due_date', 
            'priority', 
            'category', 
            'time_estimate', 
            'notify_before', 
            'attachments'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
                'rows': 3
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
                'type': 'datetime-local'
            }),
            'priority': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'time_estimate': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'notify_before': forms.TimeInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
                'type': 'time'
            }),
            'attachments': forms.FileInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
            }),
        }


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'All'),  # Allows users to show all tasks
        ('P', 'Pending'),
        ('IP', 'In Progress'),
        ('D', 'Done')
    ]
    status = forms.ChoiceField(
        choices=STATUS_CHOICES, 
        required=False, 
        label="Filter by Status",
        widget=forms.Select(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
        })
    )