from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.
def helloword(request):
    #imprime um Http resposta sem template
    return HttpResponse("hello word")

def tasklist(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request,'tasks/list.html', {'tasks': tasks})

def yourname(request, name):
    #renderiza um template com um variavel
    return render(request, 'tasks/yourname.html',{'name': name})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task':task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})
    
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)    
    
    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        
        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
      return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    