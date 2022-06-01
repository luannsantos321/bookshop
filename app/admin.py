from django.contrib import admin
from app.models import Livros
# Register your models here.


class LivrosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'paginas', 'data_publicacao', 'criacao_dados')
    list_filter = ('id', 'titulo', 'autor', 'paginas', 'data_publicacao', 'criacao_dados')


admin.site.register(Livros, LivrosAdmin)