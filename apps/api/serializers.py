from rest_framework import serializers
from todo.models import task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ("name","token","done")

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ("name","detail","time_to_start","time_to_finish")