from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("", views.ProjectList.as_view(), name="project_list"),
    path("tasks/<str:token>/", views.ProjectTaskList.as_view(), name="project_task_list"),

    path("update-project/<str:token>/", views.UpdateProject.as_view(),name="update_project"),

    path("create-project/", views.CreateProject.as_view(), name='create_project'),
    path("create-project-task/<str:token>/", views.CreateProjectTask.as_view(), name='create_project_task'),

    path("delete-project/<str:token>/", views.DeleteProject.as_view(),name="delete_project"),

]