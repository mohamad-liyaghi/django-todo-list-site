from django.urls import path
from .views.task_views import (TaskView, TaskAdd, TaskDetail, TaskDelete, TaskUpdateStatus, TaskAutoDelete)
from .views.other_views import (ApiHomeView, tbLoginApi, tbLoginEmailApi, tbLogoutApi, tbRegisterApi, ApiView)
from .views.project_views import (ProjectView, ProjectAdd, ProjectDetail, ProjectDelete, ProjectAddTask)

app_name = "api"

urlpatterns= [
    path("", ApiHomeView.as_view(), name="home-api"),
    path("api/", ApiView, name="api-list"),

    path("task-list/<str:owner>/", TaskView.as_view(), name="task-api"),
    path("project-list/<str:owner>/", ProjectView.as_view(), name="project-api"),

    path("create-task/<str:owner>/", TaskAdd.as_view(), name="task-add"),
    path("project-add/<str:owner>/", ProjectAdd.as_view(), name="project-add"),
    
    path("detail-task/<str:token>/<str:owner>/", TaskDetail.as_view(), name="task-detail"),
    path("project-detail/<str:token>/<str:owner>/", ProjectDetail.as_view(), name="project-detail"),

    path("update-task/<str:token>/<str:owner>/",TaskUpdateStatus, name="task-update"),
    path("delete-task/<str:token>/<str:owner>/",TaskDelete.as_view(), name="task-delete"),
    path("delete-project/<str:token>/<str:owner>/",ProjectDelete.as_view(), name="project-delete"),
    
    path("project-add-task/<str:owner>/<str:project_token>/<str:task_token>/",ProjectAddTask.as_view(), name="project-add-task"),

    path("auto-delete-task/<str:owner>/",TaskAutoDelete.as_view(), name="task-auto-delete"),
    path("tb-login/<str:username>/<str:token>/<int:userid>/",tbLoginApi, name="tb-login"),
    path("tb-login-email/<str:email>/<str:token>/<int:userid>/",tbLoginEmailApi, name="tb-login-email"),
    path("tb-logout/<str:username>/<str:token>/<int:userid>/",tbLogoutApi, name="tb-logout"),
    path("tb-register/",tbRegisterApi.as_view(), name="tb-register"),
]
