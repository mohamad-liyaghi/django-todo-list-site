from django.urls import path

from . import  views


app_name = "task"

urlpatterns = [
    path("", views.TaskList.as_view(), name="home"),
    # path("list-project/", listProject.as_view(), name="listProject"),
    # path("list-project-task/<str:token>/", ListProjectTask.as_view(), name="listProjectTask"),

    path("update-task/<str:token>/", views.UpdateTask.as_view(), name="update_task"),
    # path("update-project/<str:token>/", UpdateProject.as_view(),name="updateProject"),

    path("create-task/", views.CreateTask.as_view(), name="create_task"),
    # path("create-project/", CreateProject.as_view(), name='CreateProject'),
    # path("create-project-task/<str:token>/", CreateProjectTask.as_view(), name='CreateProjectTask'),

    path("delete-task/<str:token>/", views.DeleteTask.as_view(),name="delete_task"),
    # path("delete-project/<str:token>/",DeleteProject.as_view(),name="DeleteProject"),
    
    path("search/", views.SearchTask.as_view(), name="search_task"),

    # path('token/', Token.as_view(),name="token"),
    # path('token/change/', ChangeToken.as_view(),name="change-token")
]