from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Task(models.Model):
    
    
    STATUS = (
        ('doing','fazendo'),
        ('done','feito'),
    )
    
    title = models.CharField(max_length=255,)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    
    #id do usuário
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    #insere a data de criação
    created_at = models.DateTimeField(auto_now_add=True)
    #insere data para edição
    update_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title