from django.urls import path
from .views import TaskView
app_name = "api"
urlpatterns= [
    path("<str:token>/tasks/", TaskView.as_view(),name="task-api")
]