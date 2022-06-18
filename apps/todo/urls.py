from django.urls import path
from todo.views import (home_page,
                        updateTask, CreateTask, DeleteTask, SearchTask,
                        CreateProject)
app_name = "todo"

urlpatterns = [
    path("",home_page.as_view(),name="home"),
    path("update-task/<str:token>/",updateTask.as_view(),name="updateTask"),
    path("create-task/",CreateTask.as_view(),name="CreateTask"),
    path("create-project/", CreateProject.as_view(), name='CreateProject'),
    path("delete-task/<str:token>/",DeleteTask.as_view(),name="DeleteTask"),
    path("search/",SearchTask.as_view(),name="SearchTask")
]