from django.urls import path

from . import  views

# from .views.project_views import (listProject, ListProjectTask,
#                                   CreateProject, CreateProjectTask, UpdateProject, DeleteProject)
#
# from .views.routine_views import (listRoutine,
#                                      CreateRoutine, UpdateRoutine, DeleteRoutine, )
#
# from .views.token_views import(
#     ChangeToken, Token
# )


app_name = "task"

urlpatterns = [
    path("", views.TaskList.as_view(), name="home"),
    # path("list-project/", listProject.as_view(), name="listProject"),
    # path("list-project-task/<str:token>/", ListProjectTask.as_view(), name="listProjectTask"),
    # path("list-routine/", listRoutine.as_view(), name="listRoutine"),

    path("update-task/<str:token>/", views.UpdateTask.as_view(), name="update_task"),
    # path("update-project/<str:token>/", UpdateProject.as_view(),name="updateProject"),
    # path("update-routine/<str:token>/", UpdateRoutine.as_view(),name="updateRoutine"),

    path("create-task/", views.CreateTask.as_view(), name="create_task"),
    # path("create-project/", CreateProject.as_view(), name='CreateProject'),
    # path("create-project-task/<str:token>/", CreateProjectTask.as_view(), name='CreateProjectTask'),
    # path("create-routine/", CreateRoutine.as_view(), name='CreateRoutine'),

    path("delete-task/<str:token>/", views.DeleteTask.as_view(),name="delete_task"),
    # path("delete-project/<str:token>/",DeleteProject.as_view(),name="DeleteProject"),
    # path("delete-routine/<str:token>/",DeleteRoutine.as_view(),name="DeleteRoutine"),
    
    path("search/", views.SearchTask.as_view(), name="search_task"),

    # path('token/', Token.as_view(),name="token"),
    # path('token/change/', ChangeToken.as_view(),name="change-token")
]