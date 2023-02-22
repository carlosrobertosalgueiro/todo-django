from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def helloword(request):
    #imprime um Http resposta sem template
    return HttpResponse("hello word")

def tasklist(request):
    tasks = Task.objects.all()
    return render(request,'tasks/list.html', {'tasks': tasks})

def yourname(request, name):
    #renderiza um template com um variavel
    return render(request, 'tasks/yourname.html',{'name': name})