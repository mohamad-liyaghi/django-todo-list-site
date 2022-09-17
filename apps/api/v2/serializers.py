from djoser.serializers import UserCreateSerializer as BaseUserSerializer
from rest_framework import  serializers
import random

from task.models import Task


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


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "token", "status"]
