from rest_framework import serializers
from todo.models import task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = "__all__"