from django.urls import  path
from . import  views

app_name = "accounts"

urlpatterns = [
    path("token/", views.Token.as_view(), name="token"),
    path("token-gen/", views.TokenGenerator.as_view(), name="token-generator")

]
