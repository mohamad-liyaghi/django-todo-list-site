from django.urls import path
from todo.views import (home_page,
                        updateTask, CreateTask, DeleteTask, SearchTask,
                        listProject,
                        CreateProject, UpdateProject)
app_name = "todo"

urlpatterns = [
    path("",home_page.as_view(),name="home"),
    path("list-project/", listProject.as_view(), name="listProject"),
    path("update-task/<str:token>/", updateTask.as_view(),name="updateTask"),
    path("update-project/<str:token>/", UpdateProject.as_view(),name="updateProject"),
    path("create-task/",CreateTask.as_view(),name="CreateTask"),
    path("create-project/", CreateProject.as_view(), name='CreateProject'),
    path("delete-task/<str:token>/",DeleteTask.as_view(),name="DeleteTask"),
    path("search/",SearchTask.as_view(),name="SearchTask")
]