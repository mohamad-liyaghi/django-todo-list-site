from django.urls import path
from todo.views import home_page,updateTask,CreateTask,DeleteTask
app_name = "todo"
urlpatterns = [
    path("",home_page.as_view(),name="home"),
    path("update/<int:pk>/",updateTask.as_view(),name="updateTask"),
    path("create/",CreateTask.as_view(),name="CreateTask"),
    path("delete/<int:pk>/",DeleteTask.as_view(),name="DeleteTask"),


]