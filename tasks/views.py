from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
@method_decorator(login_required, name='dispatch')
class TaskView(View):
    form_class = TaskForm
    model = Task
    template_name = 'task_list.html'
    def get(self, request):
        task_list = self.model.objects.filter(creator=request.user).order_by('-created_date')
        context = {
            'task_list': task_list
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.model.objects.create(
                task=form.cleaned_data['text_input'],
                due_date=form.cleaned_data['due_date'],
                creator=request.user
            )
        return HttpResponseRedirect('/tasks')

@method_decorator(login_required, name='dispatch')
class TaskEdit(TaskView):
    def get(self, request, **kwards):
        task = get_object_or_404(self.model, pk=kwards['pk'])
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
    def post(self, request, **kwards):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.model.objects.filter(creator=request.user).filter(pk=kwards['pk']).update(
                task=form.cleaned_data['text_input'],
                due_date=form.cleaned_data['due_date'],
                is_complete=form.cleaned_data['is_complete'],
                creator=request.user
            )
        return HttpResponseRedirect('/tasks')

@method_decorator(login_required, name='dispatch')
class TaskDelete(TaskView):
    def get(self, request, **kwargs):
        get_object_or_404(self.model, creator=request.user, pk=kwargs['pk']).delete()
        return HttpResponseRedirect('/tasks')

@method_decorator(login_required, name='dispatch')
class TaskUpdateStatus(TaskView):
    def get(self, request, **kwargs):
        task = get_object_or_404(self.model, creator=request.user, pk=kwargs['pk'])
        task.is_complete = False if task.is_complete else True
        task.save()
        return HttpResponseRedirect('/tasks')
