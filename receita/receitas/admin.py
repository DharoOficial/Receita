from django.contrib import admin
from django.contrib import admin
from .models import Receita

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("Nome", "Ingredientes", "Modo_Preparo")