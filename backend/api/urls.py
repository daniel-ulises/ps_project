from django.urls import path
from . import views

urlpatterns = [
    path("cache", views.cachePs, name="cache"),
    path("get", views.getPs, name="get")
]
