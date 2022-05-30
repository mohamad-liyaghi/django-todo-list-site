from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response

import uuid

from .serializers import TaskSerializer,TaskCreateSerializer,TaskDerailSerializer
from todo.models import task
from account.models import User

class ApiHomeView(APIView):
    '''
        Available api list
    '''
    def get(self,request):
        api_list = [
            {"List of tasks:" : "api/v1/list/<user-token>/"},
            {"Tasks detail" : "/api/v1/detail/<task-token>/<task-owner>/"},
            {"Create task" : "/api/v1/create/<owner-token>/"}
        ]
        return Response(api_list)

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
        request.data._mutable = True
        data = request.data
        serializer = TaskCreateSerializer(data=data, partial=True)
        task_owner = User.objects.get(token=owner)
        if serializer.is_valid():
            serializer = serializer.save(owner=task_owner,token=uuid.uuid4().hex.upper()[0:12])
        return Response("data saved")

class TaskDetail(APIView):
    '''
        Your tasks detail
    '''
    queryset = task.objects.all()
    serializer_class = TaskCreateSerializer
    def get(self,request,owner,token):
        queryset = get_object_or_404(task, Q(token=token) & Q(owner__token=owner))
        serializer = TaskDerailSerializer(queryset, many=True)
        return Response(serializer.data)

class TaskDelete(APIView):
    '''
        Delete a task
    '''
    def get(self,request,token,owner):
        try:
            get_object_or_404(task, Q(token=token) & Q(owner__token=owner)).delete
            return Response("Task  deleted")
        except:return Response("no such task found")

def TaskUpdateStatus(request, token, owner):
    object = task.objects.filter(Q(token=token) & Q(owner__token=owner)).first()
    if object.done is not True:
        object.done = True
        object.save()
        return JsonResponse({'done': 'Task updated successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Task is already done'}, status=401)



def ApiView(request):
    '''
        a Task documentation page
    '''
    return render(request,"todo/api_list.html")
