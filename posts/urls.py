from django.contrib import admin
from django.urls import path,include
from . import views
app_name="posts"
urlpatterns = [
    path("",views.index,name="index"),
    path("register/",views.user_register,name="register"),
    path("home/",views.home,name="home"),
    path("logout/",views.user_logout,name="logout"),
    path("login/",views.user_login,name="login"),
    path("add_post/",views.add_post,name="add_post"),
    path("show_post/<int:id>/",views.show_post,name="show_post"),
    path("all_posts/",views.all_posts,name="all_posts"),
    path("delete_post/<int:id>",views.home,name="delete_post"),
    path("edit_post/<int:id>",views.edit_post,name="edit_post"),
]
