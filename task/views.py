from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def tasklist(request):
    
    search = request.GET.get('search')
    
    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    else:   
        
        #chamado todos os intems do db e ordena
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
        
        #paginação
        paginator = Paginator(tasks_list, 4)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    
    #renderização
    return render(request,'tasks/list.html', {'tasks': tasks})


@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task':task})

@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})
    
@login_required   
def editTask(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
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
  
@login_required
def deleteTAsk(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    
    messages.info(request, 'Tarefa deletada com sucesso')
    
    return redirect('/')       

def yourname(request, name):
    #renderiza um template com um variavel
    return render(request, 'tasks/yourname.html',{'name': name})

# Create your views here.
def helloword(request):
    #imprime um Http resposta sem template
    return HttpResponse("hello word")