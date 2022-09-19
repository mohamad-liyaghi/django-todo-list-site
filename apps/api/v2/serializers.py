from djoser.serializers import UserCreateSerializer as BaseUserSerializer
from rest_framework import  serializers
import random

from task.models import Task

from routine.models import Routine
from project.models import Project

# override the SignUp serializer
class UserCreateSerializer(BaseUserSerializer):
    token = serializers.CharField(read_only=True)

    class Meta(BaseUserSerializer.Meta):
        fields = ["email", "password", "token"]

    def save(self):
        '''Assign token to a user'''

        user = super().save()
        user.token = random.randint(0, 9999999999)
        user.save()
        return user


class BaseListSerializer(serializers.ModelSerializer):
    '''Base serializer fields for all List Serializers'''
    token = serializers.CharField(read_only=True)

    class Meta:
        fields = ["title", "token", "status"]


class BaseCreateSerializer(serializers.ModelSerializer):
    '''Base serializer for creating objects'''
    token = serializers.CharField(read_only=True)

    class Meta:
        fields = ["title", "detail", "time", "token"]

    def save(self):
        object = super().save()
        object.token = random.randint(0, 9999999999)
        object.owner = self.context['user']
        object.save()
        return object


class BaseDetailSerializer(serializers.ModelSerializer):
    '''Base Detail serializer class'''
    token = serializers.CharField(read_only=True)

    class Meta:
        fields = ['title', 'detail', 'token', 'status', 'time']

# --------------------Stuff related to Task Viewsets-----------------------------

class TaskListSerializer(BaseListSerializer):
    class Meta(BaseListSerializer.Meta):
        model = Task


class CreateTaskSerializer(BaseCreateSerializer):
    class Meta(BaseCreateSerializer.Meta):
        model = Task


class TaskDetailSerializer(BaseDetailSerializer):

    lookup_field = 'token'

    extra_kwargs = {
        'url': {'lookup_field': 'token'}
    }

    class Meta(BaseDetailSerializer.Meta):
        model = Task

# --------------------Serializers related to Routine ViewSet-----------------------------
class RoutineListSerializer(BaseListSerializer):
    class Meta(BaseListSerializer.Meta):
        model = Routine


class CreateRoutineSerializer(BaseCreateSerializer):
    class Meta(BaseCreateSerializer.Meta):
        model = Routine
        fields = BaseListSerializer.Meta.fields + ["task_count"]


class RoutineDetailSerializer(BaseDetailSerializer):

    lookup_field = 'token'

    extra_kwargs = {
        'url': {'lookup_field': 'token'}
    }

    class Meta(BaseDetailSerializer.Meta):
        model = Routine
# --------------------Serializers related to Project ViewSet-----------------------------
class ProjectListSerializer(BaseListSerializer):
    '''List of all Projects of a user'''

    task_count = serializers.SerializerMethodField(
        method_name='calculate_project_tasks')

    class Meta(BaseListSerializer.Meta):
        model = Project
        fields = BaseListSerializer.Meta.fields + ["task_count"]

    # calculate project tasks
    def calculate_project_tasks(self, project:Project):
        return project.task.count()


class CreateProjectSerializer(BaseCreateSerializer):
    class Meta(BaseCreateSerializer.Meta):
        model = Project


class ProjectDetailSerializer(BaseDetailSerializer):

    lookup_field = 'token'

    extra_kwargs = {
        'url': {'lookup_field': 'token'},
        'task' : {"read_only" : True},
    }


    class Meta(BaseDetailSerializer.Meta):
        model = Project
        fields = BaseDetailSerializer.Meta.fields + ["task"]
        depth = 1