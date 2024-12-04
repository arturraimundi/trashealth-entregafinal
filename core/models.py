from django.db import models

# Create your models here.
from stdimage.models import StdImageField

class PontodeColeta(models.Model):
    
    titulo = models.CharField('Título', max_length=100, blank=False)
    local = models.CharField('Endereço do ponto de coleta', max_length=200, blank=False)
    descricao = models.CharField(max_length=255, default='')
    imagem = StdImageField('imagem do local', upload_to='local_de_coleta', variations={'thumb':(250,250)})
    cnpj = models.CharField(max_length=255, default='')


    def __str__(self):
        return self.titulo
    
