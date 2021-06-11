from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import TaskSerializer,UserSerializer
from ..models import Task
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required

class ApiHome(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ApiUpdateView(generics.UpdateAPIView):
    queryset=Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.task_title = request.data.get("task_title")
        return super().update(request, *args, **kwargs)

class ApiDeleteView(DeleteView):
    model = Task
    success_url = "/api"

class UsersApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer