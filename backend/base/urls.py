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
    # notifications view
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
        "update-notification-status",
        views.NotificationStatusView.as_view(),
        name="update-notification-status",
    ),
    path(
        "mark-all-notifications-read",
        views.MarkAllNotificationsReadView.as_view(),
        name="mark-all-notifications-read",
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
        "liked-post-view/<str:post_id>/",
        views.LikedPostView.as_view(),
        name="liked-post-view",
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
    path("surveys/", views.GetSurvey.as_view(), name="get-surveys"),
    path("delete-post", views.ProfilePostListView.as_view(), name="delete-post"),
    path("change-profile", views.EditUserProfile.as_view(), name="change-profile"),
    # creating and calling comments
    path("commenting", views.CommentCreate.as_view(), name="comment-create"),
    path(
        "delete/<str:_id>/comment", views.CommentCreate.as_view(), name="delete-comment"
    ),
    path("comments", views.CommentListView.as_view(), name="comment-list"),
    path(
        "comments/<str:comment_id>",
        views.CommentCreate.as_view(),
        name="comment-update",
    ),
    # creating and calling itineraries
    path("create-itinerary", views.ItineraryCreate.as_view(), name="create-itinerary"),
    path(
        "itinerary-stop/<int:id>",
        views.ItineraryCreate.as_view(),
        name="itinerary-stop",
    ),
    path("itinerary", views.ItineraryListView.as_view(), name="itineraries"),
    # path("delete-itinerary", views.DeleteItinerary.as_view(), name="delete-itinerary"),
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
        "update-itinerary",
        views.UpdateSaveItineraryView.as_view(),
        name="update-itinerary",
    ),
    path(
        "delete-itinerary/<int:id>/<int:viewed_it_id>",
        views.ItineraryCreate.as_view(),
        name="delete-itinerary",
    ),
    path(
        "update-save-itinerary/<int:id>/saved-itinerary/<int:id_in_saved_itinerary>/",
        views.UpdateSaveItineraryAndStatus.as_view(),
        name="update-save-itinerary-and-status",
    ),
    path(
        "update/<int:id>/itinerary",
        views.UpdateSaveItineraryView.as_view(),
        name="update-itinerary-details",
    ),
    path(
        "saved-itinerary", views.SaveItineraryListView.as_view(), name="saved-itinerary"
    ),
    path("ratings/", views.SaveItineraryView.as_view(), name="update_rating"),
    path(
        "viewing-itinerary/<int:id>",
        views.ViewItinerary.as_view(),
        name="check-itinerary",
    ),
    # ADMIN
    path(
        "culturausers/all",
        views.CulturaUserAdminView.as_view(),
        name="culturauser-list-create",
    ),
    path(
        "culturauser/<int:id>/",
        views.CulturaUserAdminView.as_view(),
        name="culturauser-detail",
    ),
    path("view_user/<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),
    path(
        "user/update-privacy/", views.UpdatePrivacyView.as_view(), name="update-privacy"
    ),
    # reporting  views router
    path("reports/", views.ReportListView.as_view(), name="report-list-create"),
    path("reports/<str:pk>/", views.ReportDetailView.as_view(), name="report-detail"),
    # ADMIN
    # USER MANAGEMTN  ADMIN
    # path("viewing-itinerary", views.ViewingSaveItineraryListView.as_view(), name="viewing-itinerary"),
]
