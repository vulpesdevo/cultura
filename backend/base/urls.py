from django.urls import path, re_path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("user", views.UserView.as_view(), name="user"),
    
    path("registration", views.UserRegister.as_view(), name="registration"),
    path("login", views.UserLogin.as_view(), name="login"),
    path("logout", views.UserLogout.as_view(), name="logout"),


    # creating and calling posts
    path("posting", views.PostCreate.as_view(), name="post-create"),
    path("posts", views.PostListView.as_view(), name="post-list"),
    
    
    # creating and calling comments
    path("commenting", views.CommentCreate.as_view(), name="comment-create"),
    path("comments", views.CommentListView.as_view(), name="comment-list"),
    
    # creating and calling itineraries
    path("create-itinerary", views.ItineraryCreate.as_view(), name="create-itinerary"),
    path("itinerary", views.ItineraryListView.as_view(), name="itineraries"),
    
    path("save-itinerary", views.SaveItineraryView.as_view(), name="save-itinerary"),
    
]
