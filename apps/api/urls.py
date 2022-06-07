from django.urls import path
from .views import (ApiHomeView,ApiView,
                    TaskView,TaskAdd,TaskDetail,TaskDelete,TaskUpdateStatus,
                    tbLoginApi, tbRegisterApi, tbLogoutApi, TaskAutoDelete)
app_name = "api"
urlpatterns= [
    path("",ApiHomeView.as_view(),name="home-api"),
    path("api/",ApiView,name="api-list"),
    path("list/<str:owner>/", TaskView.as_view(),name="task-api"),
    path("create/<str:owner>/", TaskAdd.as_view(),name="task-add"),
    path("detail/<str:token>/<str:owner>/", TaskDetail.as_view(),name="task-detail"),
    path("update/<str:token>/<str:owner>/",TaskUpdateStatus, name="task-update"),
    path("delete/<str:token>/<str:owner>/",TaskDelete.as_view(), name="task-delete"),
    path("auto-delete/<str:owner>/",TaskAutoDelete.as_view(), name="task-auto-delete"),
    path("tb-login/<str:username>/<str:token>/<int:userid>/",tbLoginApi, name="tb-login"),
    path("tb-logout/<str:username>/<str:token>/<int:userid>/",tbLogoutApi, name="tb-logout"),
    path("tb-register/",tbRegisterApi.as_view(), name="tb-register"),
]
