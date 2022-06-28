from django.urls import path,include
from . import views

app_name = "accounts"
urlpatterns = [
    path('login/', views.login_user.as_view(), name="login"),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user.as_view(), name='register_user'),
]
