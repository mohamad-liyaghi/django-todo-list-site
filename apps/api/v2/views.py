from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import (TaskListSerializer, CreateTaskSerializer, TaskDetailSerializer,
                          RoutineListSerializer, CreateRoutineSerializer, RoutineDetailSerializer)

from task.models import Task
from routine.models import Routine



class TaskViewSet(ModelViewSet):
    '''ViewSet For Task Model.'''

    permission_classes = [IsAuthenticated,]
    lookup_field = 'token'


    def get_serializer_class(self):
        # check the method and return appropriate Serializer
        if self.action == "list":
            return TaskListSerializer

        elif self.action == "create":
            return CreateTaskSerializer

        elif self.action in ["retrieve", "update", "partial_update"] :
            return TaskDetailSerializer


    def get_queryset(self):
        return Task.objects \
            .filter(owner=self.request.user) \
            .order_by("status")

    def get_serializer_context(self):
        return {'user': self.request.user}



class RoutineViewSet(ModelViewSet):
    '''List/Update/Delete/Detail of a routine'''

    permission_classes = [IsAuthenticated, ]
    lookup_field = "token"

    def get_queryset(self):
        # return all routines of a user
        return Routine \
            .objects \
            .filter(owner=self.request.user) \
            .order_by("status")

    def get_serializer_class(self):
        if self.action == "list":
            return RoutineListSerializer

        elif self.action == "create":
            return CreateRoutineSerializer

        elif self.action in ["retrieve", "update", "partial_update"] :
            return RoutineDetailSerializer