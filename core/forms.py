from django import forms
from .models import PontodeColeta

class PontodeColetaForm(forms.ModelForm):
    class Meta:
        model = PontodeColeta
        fields = ['titulo', 'local', 'descricao', 'imagem', 'cnpj']

