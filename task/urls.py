from django.urls import path
#importa o views
from . import views

urlpatterns = [
   
    #Url de rota estatica sendo a rota principal
    path('', views.tasklist, name='tasklist'),
    
    path('task/<int:id>', views.taskView, name='task-view'),
    
    path('edit/<int:id>', views.editTask, name='edit-task'),
    
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    
    path('delete/<int:id>', views.deleteTAsk, name='delete-task'),
      
    path('newtask/', views.newTask, name='new-task')
]
