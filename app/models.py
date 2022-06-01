from django.db import models

# Create your models here.

class Livros(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60, verbose_name='Título')
    autor = models.CharField(max_length=60, verbose_name='Autor')
    paginas = models.IntegerField(verbose_name='Numero de Páginas')
    data_publicacao = models.DateField(verbose_name='Data de Publicação')
    criacao_dados = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'livros'