from django.urls import path
from . import views

appname ="insta"

urlpatterns=[
    path("", views.main, name="main"),
    path("new/", views.create, name="create"),
    path("like/", views.like, name='like'),
    path("add_comment/", views.add_comment, name='add_comment'),
    path("del_comment/", views.del_comment, name='del_comment'),
]