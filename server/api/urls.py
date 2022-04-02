from django.urls import path
from . import views

urlpatterns = [
    path("cache", views.cachePs, name="cache"),
    path("get", views.getPs, name="get"),
    path("get/users", views.getUsers, name="get_users"),
    path("get/<int:uid>", views.getById, name="get_by_id")
]
