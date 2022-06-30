from django.http import JsonResponse
from django.db.models import Q
from rest_framework.generics import ListAPIView

from api.serializers import ProjectSerializer
from todo.models import project

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
