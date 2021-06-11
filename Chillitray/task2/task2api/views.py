from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from .serializers import Task2Serializer
from ..models import Task2Model
from django.views.generic.edit import DeleteView

class Task2Api(generics.ListCreateAPIView):
    queryset = Task2Model.objects.all()
    serializer_class = Task2Serializer

class Tast2ApiUpdateView(generics.UpdateAPIView):
    queryset = Task2Model.objects.all()
    serializer_class = Task2Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.title = request.data.get('title')
        return super().update(request, *args, **kwargs)

class Task2ApiDeleteView(DeleteView):
    model = Task2Model
    success_url = "/task2/task2api/"

