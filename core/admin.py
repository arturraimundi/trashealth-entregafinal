from django.contrib import admin

# Register your models here.
from .models import PontodeColeta

@admin.register(PontodeColeta)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'local', 'descricao', 'imagem')