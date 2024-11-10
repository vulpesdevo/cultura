from django.urls import include, path, re_path
from . import views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"like-posts", views.PostViewSet, basename="like-posts")
router.register(r"follow", views.Following, basename="follow")
urlpatterns = [
    path("user", views.UserView.as_view(), name="user"),
    path("registration", views.UserRegister.as_view(), name="registration"),
    path("login", views.UserLogin.as_view(), name="login"),
    path("logout", views.UserLogout.as_view(), name="logout"),
    path(
        "update-information",
        views.EditUserInformation.as_view(),
        name="update-information",
    ),
    path("change-password", views.ChangePassword.as_view(), name="change-password"),
    path("user-settings", views.GetSettings.as_view(), name="user-settings"),
    # creating and calling posts
    path("posting", views.PostCreate.as_view(), name="post-create"),
    path("posting/<str:post_id>/", views.PostCreate.as_view(), name="update_post"),
    path("send-otp", views.OTPVerification.as_view(), name="send-otp"),
    path("fp-otp", views.ForgotPassword.as_view(), name="fp-otp"),
    path("fp-change", views.ChangeForgotPassword.as_view(), name="fp-change"),
    path("posts-list/", views.PostListView.as_view(), name="post-list"),
    path(
        "like-notification-list",
        views.LikesNotificationList.as_view(),
        name="like-notif-list",
    ),
    path(
        "follow-notification-list",
        views.FollowedNotification.as_view(),
        name="follow-notif-list",
    ),
    path(
        "search",
        views.SearchView.as_view(),
        name="search",
    ),
    path(
        "public-profile-posts/",
        views.PublicPostProfile.as_view(),
        name="public-profile-posts",
    ),
    path(
        "liked-post-view/<str:post_id>/<str:notif>",
        views.LikedPostView.as_view(),
        name="liked-post-view",
    ),
    path("", include(router.urls)),
    path(
        "profile-posts", views.ProfilePostListView.as_view(), name="profile-post-list"
    ),
    path("rating", views.ProfilePostListView.as_view(), name="rate-itinerary"),
    path("get-survey", views.GetSurvey.as_view(), name="get-survey"),
    path("delete-post", views.ProfilePostListView.as_view(), name="delete-post"),
    path("change-profile", views.EditUserProfile.as_view(), name="change-profile"),
    # creating and calling comments
    path("commenting", views.CommentCreate.as_view(), name="comment-create"),
    path("comments", views.CommentListView.as_view(), name="comment-list"),
    # creating and calling itineraries
    path("create-itinerary", views.ItineraryCreate.as_view(), name="create-itinerary"),
    path("itinerary", views.ItineraryListView.as_view(), name="itineraries"),
    path("delete-itinerary", views.DeleteItinerary.as_view(), name="delete-itinerary"),
    path(
        "itinerary/<int:id>",
        views.ItinerariesInView.as_view(),
        name="itineraries-in-viewing",
    ),
    # path(
    #     "follow/<int:id>",
    #     views.Following.as_view(),
    #     name="follow",
    # ),
    path("save-itinerary", views.SaveItineraryView.as_view(), name="save-itinerary"),
    path(
        "saved-itinerary", views.SaveItineraryListView.as_view(), name="saved-itinerary"
    ),
    path("ratings/", views.SaveItineraryView.as_view(), name="update_rating"),
    path(
        "viewing-itinerary/<int:id>",
        views.ViewItinerary.as_view(),
        name="check-itinerary",
    ),
    path("reports/", views.ReportListCreateView.as_view(), name="report-list-create"),
    # path("viewing-itinerary", views.ViewingSaveItineraryListView.as_view(), name="viewing-itinerary"),
]
