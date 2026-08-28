from django.urls import path, include
from . import views


app_name = "global_search"

urlpatterns = [
    path("global", views.search, name = "search")
]