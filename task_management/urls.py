from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:pk>/edit/', views.edit_task, name='edit_task'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/complete/<int:task_id>/', views.complete_task, name='complete_task'),
]
