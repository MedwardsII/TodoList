from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                task=form.cleaned_data['text_input'],
                due_date=form.cleaned_data['due_date'],
                creator=request.user
            )
    task_list = Task.objects.filter(creator=request.user).order_by('-created_date')
    context = {
        'task_list': task_list
    }
    return render(request, 'task_list.html', context)

@login_required
def task_edit(request, pk):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.filter(creator=request.user).filter(pk=pk).update(
                task=form.cleaned_data['text_input'],
                due_date=form.cleaned_data['due_date'],
                is_complete=form.cleaned_data['is_complete'],
                creator=request.user
            )
        return redirect('tasks:task_list')
    task = get_object_or_404(Task, pk=pk)
    data = {
        'pk':task.pk,
        'text_input': task.task,
        'due_date': task.due_date,
        'is_complete': task.is_complete
    }
    context = {
        'task_data': data
    }
    return render(request, 'task_edit.html', context)

@login_required
def task_delete(request, pk):
    try:
        task = Task.objects.filter(creator=request.user).filter(pk=pk)
    except:
        raise Http404
    task.delete()
    return redirect('tasks:task_list')

@login_required
def task_update_stats(request, pk):
    try:
        task = Task.objects.filter(creator=request.user).filter(pk=pk)
    except:
        raise Http404
    if task.is_complete:
        task.is_complete = False
    else:
        task.is_complete = True
    task.save()
    return redirect('tasks:task_list')