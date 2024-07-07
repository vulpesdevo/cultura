from django.urls import include, path, re_path
from . import views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'like-posts', views.PostViewSet, basename='like-posts')

urlpatterns = [
    path("user", views.UserView.as_view(), name="user"),
    
    path("registration", views.UserRegister.as_view(), name="registration"),
    path("login", views.UserLogin.as_view(), name="login"),
    path("logout", views.UserLogout.as_view(), name="logout"),


    # creating and calling posts
    path("posting", views.PostCreate.as_view(), name="post-create"),
    path("posts-list/", views.PostListView.as_view(), name="post-list"),
    path("like-notification-list", views.LikesNotificationList.as_view(), name="like-notif-list"),
    path("liked-post-view/<str:post_id>/", views.LikedPostView.as_view(), name="liked-post-view"),
    path('', include(router.urls)),
    path("profile-posts", views.ProfilePostListView.as_view(), name="profile-post-list"),
    
    # creating and calling comments
    path("commenting", views.CommentCreate.as_view(), name="comment-create"),
    path("comments", views.CommentListView.as_view(), name="comment-list"),
    
    
    # creating and calling itineraries
    path("create-itinerary", views.ItineraryCreate.as_view(), name="create-itinerary"),
    path("itinerary", views.ItineraryListView.as_view(), name="itineraries"),
    path("itinerary/<int:id>", views.ItinerariesInView.as_view(), name="itineraries-in-viewing"),
    
    path("save-itinerary", views.SaveItineraryView.as_view(), name="save-itinerary"),
    path("saved-itinerary", views.SaveItineraryListView.as_view(), name="saved-itinerary"),
    path("viewing-itinerary/<int:id>", views.ViewItinerary.as_view(), name="check-itinerary"),
    # path("viewing-itinerary", views.ViewingSaveItineraryListView.as_view(), name="viewing-itinerary"),
    
]
