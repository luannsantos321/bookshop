from django.shortcuts import render
from app.serializers import LivrosSerializer
from app.models import Livros
# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class LivrosListGeneric(ListCreateAPIView):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class LivrosDetailGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
