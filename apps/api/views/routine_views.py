from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

import uuid

from api.serializers import RoutineSerializer, RoutineCreateSerializer, RoutineDetailSerializer
from routine.models import Routine
from accounts.models import User

class RoutineView(ListAPIView):
    '''
        Show all routines
    '''
    model = Routine
    serializer_class = RoutineSerializer
    def get_queryset(self):
        owner = self.kwargs["owner"]
        object = Routine.objects.filter(Q(owner__token=owner))
        return object

class RoutineAdd(CreateAPIView):
    '''
        Create routine
    '''
    queryset = Routine.objects.all()
    serializer_class = RoutineCreateSerializer
    def create(self,request,owner):
        data = self.request.data
        serializer = RoutineCreateSerializer(data=data, partial=True)
        routine_owner = User.objects.get(token=owner)
        if serializer.is_valid():
            serializer = serializer.save(owner=routine_owner ,token=uuid.uuid4().hex.upper()[0:12])
            return JsonResponse({"token" : serializer.token})
        else:
            return JsonResponse({"error" : "sth is wrong with your information"})

class RoutineDetail(APIView):
    '''
        Your routine detail
    '''
    queryset = Routine.objects.all()
    serializer_class = RoutineDetailSerializer
    def get(self,request,owner,token):
        queryset = Routine.objects.filter(Q(token=token) & Q(owner__token=owner))
        serializer = RoutineDetailSerializer(queryset, many=True)
        return Response(serializer.data)

class RoutineDelete(APIView):
    '''
        Delete a Routine
    '''
    def get(self,request,token,owner):
        try:
            Routine.objects.filter(Q(token=token) & Q(owner__token=owner))
            return Response("routine  deleted")
        except:return Response("no such routine found")

