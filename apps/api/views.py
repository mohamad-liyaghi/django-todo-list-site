from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
import uuid

from .serializers import TaskSerializer,TaskCreateSerializer,TaskDerailSerializer
from todo.models import task
from account.models import User

class ApiHomeView(APIView):
    def get(self,request):
        return Response("""
        Api guide: List of tasks: domain.com/list/<user-token>/ 
        Tasks detail: domain.com/api/v1/detail/<task-token>/<task-owner>/ 
        Create task: domain.com/api/v1/create/<owner-token>/
        """)

class TaskView(APIView):
    model = task
    serializer_class = TaskSerializer
    def get(self,request,owner):
        queryset = task.objects.filter(owner__token=owner)
        serializer = TaskSerializer(queryset,many=True)
        return Response(serializer.data)

class TaskAdd(generics.CreateAPIView):
    queryset = task.objects.all()
    serializer_class = TaskCreateSerializer
    def create(self,request,owner):
        request.data._mutable = True
        data = request.data
        serializer = TaskCreateSerializer(data=data, partial=True)
        task_owner = User.objects.get(token=owner)
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

class TaskDelete(APIView):
    def get(self,request,token,owner):
        try:
            task.objects.get(token=token,owner__token=owner).delete()
            return Response("Task has deleted")
        except:return Response("no such task found")

def ApiView(request):
    return render(request,"todo/api_list.html")
