from django.urls import path, include
from . import views


app_name = "portfolio"

urlpatterns = [
    path("detail/<str:slug>", views.Project_detail, name="project_detail")
]