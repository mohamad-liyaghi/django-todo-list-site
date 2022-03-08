from django.urls import path
from .views import home_page,detail
app_name = "todo"
urlpatterns = [
    path("",home_page.as_view(),name="home"),
    path("<int:pk>/",detail.as_view(),name="detail")

]