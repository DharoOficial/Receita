from django.contrib.auth.models import User
from django.db import models

class Receita(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=255)
    Ingredientes = models.CharField(max_length=300)
    Modo_Preparo = models.CharField(max_length=300)

def BuscarID(self):
    return self.Id

def BuscarAutor(self):
    return self.author
    