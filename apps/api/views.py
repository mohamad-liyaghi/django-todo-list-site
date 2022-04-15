from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import TaskSerializer
from todo.models import task

class TaskView(APIView):
    model = task
    serializer_class = TaskSerializer
    def get(self,request,token):
        queryset = task.objects.filter(owner__token=token)
        serializer = TaskSerializer(queryset,many=True)
        return Response(serializer.data)

