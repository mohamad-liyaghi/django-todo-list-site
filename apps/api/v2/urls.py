from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

app_name = "api_v2"


router = routers.DefaultRouter()

router.register('task', views.TaskViewSet, basename="task")
router.register('routine', views.RoutineViewSet, basename="routine")
router.register('project', views.ProjectViewSet, basename="project")



urlpatterns = router.urls
