from django.urls import path
from .views import TaskView,TaskAdd,TaskDetail
app_name = "api"
urlpatterns= [
    path("tasks/<str:token>/", TaskView.as_view(),name="task-api"),
    path("create/<str:token>/", TaskAdd.as_view(),name="task-add"),
    path("detail/<str:token>/<str:owner>/", TaskDetail.as_view(),name="task-detail"),
]