from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Task, Category
from .forms import TaskForm, TaskFilterForm

# Create your views here.

@staff_member_required
def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        Category.objects.create(name=name, description=description)
        return redirect('category_list')

    return render(request, 'task_management/create_category.html')


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  
            task.save()
            form.save_m2m()  
            return redirect('task_list')  
    else:
        form = TaskForm()

    context = {
        'form': form
    }
    return render(request, 'task_management/create_task.html', context)


@login_required
def task_list(request):
    # Initialize the filter form
    filter_form = TaskFilterForm(request.GET)

    # Get tasks only created by the logged-in user
    tasks = Task.objects.filter(user=request.user)

    # If a status filter is applied
    if filter_form.is_valid() and filter_form.cleaned_data['status']:
        tasks = tasks.filter(status=filter_form.cleaned_data['status'])

    context = {
        'tasks': tasks,
        'filter_form': filter_form,
    }
    return render(request, 'task_management/task_list.html', context)


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = 'D'  # Mark task as 'Done'
    task.save()
    return redirect('task_list')


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Make sure only the current user's tasks can be edited
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'task_management/edit_task.html', context)
