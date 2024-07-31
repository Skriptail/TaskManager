from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Task Manager', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Something went wrong with form'

    form = TaskForm()
    context = {
        'form': form


    }
    return render(request, 'main/create.html', context)

# Create your views here.
