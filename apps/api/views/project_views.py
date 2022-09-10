from django.http import JsonResponse
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView

from api.serializers import ProjectSerializer, ProjectCreateSerializer, ProjectDetailSerializer

import uuid

from task.models import project, Task
from accounts.models import User

class ProjectView(ListAPIView):
    '''
        Show all projects
    '''
    model = project
    serializer_class = ProjectSerializer
    def get_queryset(self):
        owner = self.kwargs["owner"]
        object = project.objects.filter(Q(owner__token=owner))
        return object



class ProjectAdd(CreateAPIView):
    '''
        Create project
    '''
    queryset = project.objects.all()
    serializer_class = ProjectCreateSerializer
    def create(self,request,owner):
        data = self.request.data
        serializer = ProjectCreateSerializer(data=data, partial=True)
        project_owner = User.objects.get(token=owner)
        if serializer.is_valid():
            serializer = serializer.save(owner=project_owner, token=uuid.uuid4().hex.upper()[0:12])
            return JsonResponse({"token" : serializer.token})
        else:
            return JsonResponse({"error" : "sth is wrong with your information"})

class ProjectDetail(APIView):
    '''
        Project datail
    '''
    queryset = project.objects.all()
    serializer_class = ProjectDetailSerializer

    def get(self,request,owner,token):
        queryset = project.objects.filter(Q(token=token) & Q(owner__token=owner))
        serializer = ProjectDetailSerializer(queryset, many=True)
        return Response(serializer.data)

class ProjectDelete(APIView):
    '''
        Delete a project
    '''
    def get(self,request,token,owner):
        try:
            project.objects.filter(Q(token=token) & Q(owner__token=owner)).delete()
            return Response("project  deleted")
        except:return Response("no such project found")

class ProjectAddTask(APIView):
    '''
        Add task to a project
    '''
    def post(self, request, owner, project_token, task_token):
        try:
            project_model = project.objects.filter(Q(token= project_token) & Q(owner__token=owner)).first()
            task_model = Task.objects.filter(Q(token= task_token)).first()
            project_model.task.add(task_model)
            return JsonResponse({"done" : "task added to project"})
        except:
            return JsonResponse({"error" : "sth went wrong with your information"})