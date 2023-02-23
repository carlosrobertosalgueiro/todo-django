from django.urls import path
#importa o views
from . import views

urlpatterns = [
    #Url de rota estática
    path('helloword/', views.helloword ),
    #Url de rota estatica sendo a rota principal
    path('', views.tasklist, name='tasklist'),
    #recebe uma valor via url
    path('stringname/<str:name>', views.yourname, name='yourname'),
    
    path('task/<int:id>', views.taskView, name='task-view'),
    
    path('newtask/', views.newTask, name='new-task')
]
