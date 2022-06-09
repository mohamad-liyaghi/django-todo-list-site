from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response

import uuid

from .serializers import TaskSerializer,TaskCreateSerializer,TaskDerailSerializer,RegisterUserSerializer
from todo.models import task
from account.models import User
from account.models import User

class ApiHomeView(APIView):
    '''
        Available api list
    '''
    def get(self,request):
        api_list = [
            {"List of tasks:" : "api/v1/list/<user-token>/"},
            {"Tasks detail" : "/api/v1/detail/<task-token>/<task-owner>/"},
            {"Create task" : "/api/v1/create/<owner-token>/"},
            {"Update your tasks status" : "/api/v1/update/<task-token>/<owner-token>/"}
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
        serializer = TaskDerailSerializer(queryset, many=True)
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

def tbLoginApi(request, username, token, userid):
    '''
        This page check if a user is registered or no
        then it will be proccessed in the telegram bot
    '''
    user = User.objects.filter(Q(token=token) & Q(username=username)).first()
    if user:
        if user.telegram_id is None:
            user.telegram_id = userid
            user.save()
            return JsonResponse({"found" : "user exist in db"})
        else:
            return JsonResponse({"login-error": "user is already logged in"})
    else:
        return JsonResponse({"error" : "user does not exist"})


def tbLogoutApi(request, username, token, userid):
    '''
        This page check if a user is registered or no
        then it will be proccessed in the telegram bot
    '''
    user = User.objects.filter(Q(token=token) & Q(username=username)).first()
    if user:
        if user.telegram_id == userid:
            user.telegram_id = None
            user.save()
            return JsonResponse({"done" : "user logged out"})
        else:
            return JsonResponse({"userid-error": "user id is wrong"})
    else:
        return JsonResponse({"error" : "user does not exist"})

class tbRegisterApi(CreateAPIView):
    '''
        Tb users can register by this api
    '''
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer




def ApiView(request):
    '''
        a Task documentation page
    '''
    return render(request,"todo/api_list.html")
