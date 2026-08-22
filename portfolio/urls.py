from django.urls import path, include
from . import views


app_name = "portfolio"

urlpatterns = [
    path("detail/<slug:slug>", views.Project_detail, name="project_detail")
]