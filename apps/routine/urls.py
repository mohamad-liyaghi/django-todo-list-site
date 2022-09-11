from django.urls import  path
from . import  views

app_name = "routine"

urlpatterns = [
    path("", views.RoutineList.as_view(), name="routine_list"),

    path("update-routine/<str:token>/", views.UpdateRoutine.as_view(), name="update_routine"),

    path("create-routine/", views.CreateRoutine.as_view(), name='create_routine'),

    path("delete-routine/<str:token>/", views.DeleteRoutine.as_view(), name="delete_routine"),


]
