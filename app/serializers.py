from rest_framework import serializers
from app.models import Livros
class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'
