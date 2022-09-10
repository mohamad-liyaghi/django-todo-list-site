from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

import uuid

from api.serializers import TaskSerializer, TaskCreateSerializer, TaskDetailSerializer
from task.models import task
from accounts.models import User

class TaskView(ListAPIView):
    '''
        Show all tasks
    '''
    model = task
    serializer_class = TaskSerializer
    def get_queryset(self):
        owner = self.kwargs["owner"]
        object = task.objects.filter(Q(owner__token=owner))
        return object

class TaskAdd(CreateAPIView):
    '''
        Create task
    '''
    queryset = task.objects.all()
    serializer_class = TaskCreateSerializer
    def create(self,request,owner):
        data = self.request.data
        serializer = TaskCreateSerializer(data=data, partial=True)
        task_owner = User.objects.get(token=owner)
        if serializer.is_valid():
            serializer = serializer.save(owner=task_owner,token=uuid.uuid4().hex.upper()[0:12])
            return JsonResponse({"token" : serializer.token})
        else:
            return JsonResponse({"error" : "sth is wrong with your information"})

class TaskDetail(APIView):
    '''
        Your tasks detail
    '''
    queryset = task.objects.all()
    serializer_class = TaskCreateSerializer
    def get(self,request,owner,token):
        queryset = task.objects.filter(Q(token=token) & Q(owner__token=owner))
        serializer = TaskDetailSerializer(queryset, many=True)
        return Response(serializer.data)

class TaskDelete(APIView):
    '''
        Delete a task
    '''
    def get(self,request,token,owner):
        try:
            task.objects.filter(Q(token=token) & Q(owner__token=owner)).delete()
            return Response("Task  deleted")
        except:return Response("no such task found")

class TaskAutoDelete(APIView):
    '''
        Remove done tasks
    '''
    def get(self,request,owner):
            obj = get_object_or_404(task, Q(owner__token=owner) & Q(done=True))
            obj.delete()
            return Response("some tasks removed")


def TaskUpdateStatus(request, token, owner):
    object = task.objects.filter(Q(token=token) & Q(owner__token=owner)).first()
    if object.done is not True:
        object.done = True
        object.save()
        return JsonResponse({'done': 'Task updated successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Task is already done'}, status=401)
