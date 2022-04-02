from django.urls import path
from . import views

# Following routes are:
# cache: Execute the bash script to fill the database with running processes
# get/ps: Get the saved processes
# get/users: Get users with a process attatched to them
# get/<int:uid>: Get running processes attatched to a user, by their UID
urlpatterns = [
    path("cache", views.cachePs, name="cache"),
    path("get/ps", views.getPs, name="get"),
    path("get/users", views.getUsers, name="get_users"),
    path("get/<int:uid>", views.getById, name="get_by_id")
]
