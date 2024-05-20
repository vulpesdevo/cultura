from django.urls import path, re_path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("user", views.UserView.as_view(), name="user"),
    path("registration", views.UserRegister.as_view(), name="registration"),
    path("login", views.UserLogin.as_view(), name="login"),
    path("logout", views.UserLogout.as_view(), name="logout"),
    path("posts/create/", views.PostCreate.as_view(), name="post-create"),
    path(
        "posts/<int:post_id>/comments/create/",
        views.CommentCreate.as_view(),
        name="api-comment-create",
    ),
]
