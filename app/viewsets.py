from rest_framework import viewsets
from app.serializers import LivrosSerializer
from app.models import Livros

class LivrosViewset(viewsets.ModelViewSet):
    serializer_class = LivrosSerializer
    queryset = Livros.objects.all()