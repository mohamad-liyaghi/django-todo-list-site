from rest_framework import serializers
import uuid

from todo.models import task
from account.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ("name","token","done")

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ("name","detail","time_to_start")

class TaskDerailSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ("name","detail","time_to_start","done","token")

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