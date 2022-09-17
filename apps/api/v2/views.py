from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskListSerializer

from task.models import Task



class TaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,]

    def get_serializer_class(self):
        # check the method and return appropriate Serializer
        if self.request.method == "GET":
            return TaskListSerializer

    def get_queryset(self):
        return Task.objects \
            .filter(owner=self.request.user) \
            .order_by("status")

