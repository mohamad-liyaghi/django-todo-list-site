from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
import uuid

from .serializers import TaskSerializer,TaskCreateSerializer,TaskDerailSerializer
from todo.models import task
from account.models import User

class TaskView(APIView):
    model = task
    serializer_class = TaskSerializer
    def get(self,request,token):
        queryset = task.objects.filter(owner__token=token)
        serializer = TaskSerializer(queryset,many=True)
        return Response(serializer.data)

class TaskAdd(generics.CreateAPIView):
    queryset = task.objects.all()
    serializer_class = TaskCreateSerializer
    def create(self,request,token):
        request.data._mutable = True
        data = request.data
        serializer = TaskCreateSerializer(data=data, partial=True)
        task_owner = User.objects.get(token=token)
        if serializer.is_valid():
            serializer = serializer.save(owner=task_owner,token=uuid.uuid4().hex.upper()[0:12])
        return Response("data saved")

class TaskDetail(APIView):
    queryset = task.objects.all()
    serializer_class = TaskCreateSerializer
    def get(self,request,owner,token):
        queryset = task.objects.filter(token=token, owner__token=owner)
        serializer = TaskDerailSerializer(queryset, many=True)
        return Response(serializer.data)
