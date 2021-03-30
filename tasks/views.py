# from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
# class based views
class TaskList(ListView):
    model = Task 
    context_object_name = 'tasks' # rename object_list

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'# rename the original django template name

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

# function based views
'''
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)
'''