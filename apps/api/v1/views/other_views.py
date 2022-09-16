from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.v1.serializers import RegisterUserSerializer
from accounts.models import User


class ApiHomeView(APIView):
    '''
        Available api list
    '''
    def get(self,request):
        api_list = [
            {"List of tasks:" : "api/v1/task-list/<user-token>/"},
            {"Tasks detail" : "/api/v1/detail-task/<task-token>/<task-owner>/"},
            {"Create task" : "/api/v1/create-task/<owner-token>/"},
            {"Update your tasks status" : "/api/v1/update-task/<task-token>/<owner-token>/"}
        ]
        return Response(api_list)



def tbLoginApi(request, username, token, userid):
    '''
        This page check if a user is registered or no
        then it will be proccessed in the telegram bot
    '''
    user = User.objects.filter(Q(token=token) & Q(username=username)).first()
    if user:
        if user.telegram_id is None:
            user.telegram_id = userid
            user.save()
            return JsonResponse({"found" : "user exist in db"})
        else:
            return JsonResponse({"login-error": "user is already logged in"})
    else:
        return JsonResponse({"error" : "user does not exist"})


def tbLoginEmailApi(request, email, token, userid):
    '''
        This page check if a user is registered or no
        then it will be proccessed in the telegram bot
    '''
    user = User.objects.filter(Q(token=token) & Q(email=email)).first()
    if user:
        if user.telegram_id is None:
            user.telegram_id = userid
            user.save()
            return JsonResponse({"found" : "user exist in db"})
        else:
            return JsonResponse({"login-error": "user is already logged in"})
    else:
        return JsonResponse({"error" : "user does not exist"})


def tbLogoutApi(request, username, token, userid):
    '''
        This page check if a user is registered or not
        then it will be proccessed in the telegram bot
    '''
    user = User.objects.filter(Q(token=token) & Q(username=username)).first()
    if user:
        if user.telegram_id == userid:
            user.telegram_id = None
            user.save()
            return JsonResponse({"done" : "user logged out"})
        else:
            return JsonResponse({"userid-error": "user id is wrong"})
    else:
        return JsonResponse({"error" : "user does not exist"})


class tbRegisterApi(CreateAPIView):
    '''
        Tb users can register by this api
    '''
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer




def ApiView(request):
    '''
        a Task documentation page
    '''
    return render(request,"task/api_list.html")
