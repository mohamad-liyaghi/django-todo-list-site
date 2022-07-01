from rest_framework import serializers
import uuid

from todo.models import task, project, routine
from accounts.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ("name","token","done")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ("name","token","deadline")

class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = routine
        fields = ("title","detail","token")

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ("name","detail","time_to_start")

class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ("name","detail","deadline")

class RoutineCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = routine
        fields = ("title","detail","time", "days")

class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ("name","detail","time_to_start","done","token")

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ("name","detail","deadline","status","task","token")

class RoutineDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = routine
        fields = ("title","detail","token","days","time")

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        password = serializers.ReadOnlyField()
        fields = ('username', 'first_name', 'last_name','telegram_id', "token", "password" )

    def create(self, validated_data):
        '''
            Register for tb users
        '''
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.username = first_name+last_name + uuid.uuid4().hex.upper()[0:4]
        user.first_name = first_name
        user.last_name = last_name
        user.token = uuid.uuid4().hex.upper()[0:12]
        user.save()
        return user
