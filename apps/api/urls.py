from django.urls import path
from .views import TaskView,TaskAdd
app_name = "api"
urlpatterns= [
    path("<str:token>/tasks/", TaskView.as_view(),name="task-api"),
    path("<str:token>/create/", TaskAdd.as_view(),name="task-add"),
]