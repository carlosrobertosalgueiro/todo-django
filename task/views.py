from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloword(request):
    #imprime um Http resposta sem template
    return HttpResponse("hello word")

def tasklist(request):
    #renderiza um template estático
    return render(request,'tasks/list.html')

def yourname(request, name):
    #renderiza um template com um variavel
    return render(request, 'tasks/yourname.html',{'name': name})