from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    )

from .models import Task

from .serializers import TaskSerializer

class TaskListApiView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

class TaskCreateApiView(CreateAPIView):
    serializer_class = TaskSerializer

class TaskRetrieveApiView(RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskDeleteView(DestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskUpdateView(UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

