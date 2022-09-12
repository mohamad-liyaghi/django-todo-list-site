from django.urls import path

from . import  views


app_name = "task"

urlpatterns = [
    path("", views.TaskList.as_view(), name="home"),

    path("update-task/<str:token>/", views.UpdateTask.as_view(), name="update_task"),

    path("create-task/", views.CreateTask.as_view(), name="create_task"),

    path("delete-task/<str:token>/", views.DeleteTask.as_view(),name="delete_task"),
    
    path("search/", views.SearchTask.as_view(), name="search_task"),

]