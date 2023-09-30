from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogpage, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome")
]
