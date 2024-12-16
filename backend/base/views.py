from gc import get_objects
import json
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.forms import ValidationError
from django.http import Http404, HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import (
    CulturaUserSerializer,
    FollowSerializer,
    ItinerarySerializer,
    LikeSerializer,
    SaveItinerarySerializer,
    SettingSerializer,
    SurveySerializer,
    UserRegisterSerializer,
    UserLoginSerializer,
    UserSerializer,
    PostSerializer,
    CommentSerializer,
    ReportSerializer,
)
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status, viewsets
from .validations import custom_validation, validate_username, validate_password
from .models import (
    FollowingNotification,
    Itinerary,
    LikeNotification,
    Post,
    Comment,
    CulturaUser,
    Report,
    SaveItinerary,
    Survey,
    UserSetting,
)
from bson import ObjectId
from .permissions import IsAdminUser  # Import the custom permission class

# from profanity.validators import validate_is_profane


# ADMIN
class CulturaUserAdminView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self, request, pk=None):
        if pk:
            cultura_user = get_object_or_404(CulturaUser, pk=pk)
            serializer = CulturaUserSerializer(
                cultura_user, context={"request": request}
            )
        else:
            cultura_users = CulturaUser.objects.all()
            serializer = CulturaUserSerializer(
                cultura_users, many=True, context={"request": request}
            )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = CulturaUserSerializer(data=data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        cultura_user = get_object_or_404(CulturaUser, pk=pk)
        serializer = CulturaUserSerializer(
            cultura_user, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cultura_user = get_object_or_404(CulturaUser, pk=pk)
        cultura_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# REPORT MANAGEMENT
class ReportListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data.copy()  # Make a mutable copy of the request data
        cultura_user = get_object_or_404(CulturaUser, user=request.user)
        data["user_id"] = cultura_user.id  # Set the user_id field to the CulturaUser id
        data["post_id"] = str(data["post_id"])  # Ensure post_id is a string
        serializer = ReportSerializer(data=data, context={"request": request})
        print(" SERIALIZER:", serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        report = get_object_or_404(Report, pk=pk)
        serializer = ReportSerializer(report)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        report = get_object_or_404(Report, pk=pk)
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = get_object_or_404(Post, _id=ObjectId(pk))
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ADMIN
class UpdatePrivacyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        cultura_user = get_object_or_404(CulturaUser, user=request.user)

        is_private = request.data.get("is_private")
        if is_private is not None:
            cultura_user.is_private = is_private
            cultura_user.save()
            serializer = CulturaUserSerializer(
                cultura_user, context={"request": request}
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
    )

    ##
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)

        # Get the CulturaUser profile associated with the authenticated user
        cultura_user = get_object_or_404(CulturaUser, user=user)
        profile_serializer = CulturaUserSerializer(
            cultura_user, context={"request": request}
        )

        # Update the user photo URL to be an absolute URI
        profile_data = profile_serializer.data
        if user_photo := profile_data.get("user_photo"):
            abs_image_url = request.build_absolute_uri(user_photo)
            profile_data["user_photo"] = abs_image_url
        else:
            profile_data["user_photo"] = None
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "user": serializer.data,
                "userfullname": cultura_user.fullname,
                "profile": profile_data,
                "token": token.key,
            },
            status=status.HTTP_200_OK,
        )


class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        cultura_user = get_object_or_404(CulturaUser, pk=pk)
        serializer = CulturaUserSerializer(
            cultura_user, context={"request": request, "user": request.user}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePassword(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        # username = data["password"].strip()
        # email = data["email"].strip()

        password = data["password"].strip()
        new_password = data["new_password"].strip()

        user = request.user

        if user.check_password(password) and new_password == password:
            return Response(
                {"error": "The new password is the same as the old password."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if password and not user.check_password(password):
            return Response(
                {"error": "Old password is incorrect."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # if username:
        #     user.username = username
        if password:
            user.set_password(new_password)
        user.save()

        return Response(status=status.HTTP_200_OK)


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data

        fullname = data["fullname"].strip()
        country = data["country"].strip()

        email = data["email"].strip()
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            if user := serializer.create(clean_data):
                CulturaUser.objects.create(
                    user=user,
                    fullname=fullname,
                    country=country,
                    email=email,
                    #  # Assuming you want to associate the Profile with the created user
                )
                UserSetting.objects.create(user=user)
                login(request, user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                # return Response({"user": serializer.data})
        return Response(status=status.HTTP_400_BAD_REQUEST)


# FORGOT PASSWORD
# users = UserModel.objects.filter(email=email)
class ChangeForgotPassword(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        email = data.get("email", "").strip()
        user = UserModel.objects.get(email=email)
        new_password = data.get("password", "").strip()
        # print(user)
        # email = data.get("email", "").strip()
        if new_password:
            user.set_password(new_password)
        user.save()
        return Response(status=status.HTTP_200_OK)


class ForgotPassword(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        email = data["email"].strip()
        # print(email)
        if UserModel.objects.filter(email=email):

            from email.message import EmailMessage
            import ssl
            import smtplib
            import random
            import math
            import certifi

            # generating OTP 6 digit code

            otp = random.randint(100000, 999999)

            print("OTP:", otp)

            # SENDING TO EMAIL
            email_sender = "culturalink62@gmail.com"
            email_password = "syhj wqky hzwz kllz"
            email_receiver = email
            subject = "Request to Change Password for CulturaLink "

            body = (
                "Seems like you forgot your password!\nEnter the following code in your Cultura Application:\n\n\n"
                + str(otp)
                + "\n\n\nif you did not request this please send us an email to this address right away"
            )

            EM = EmailMessage()
            EM["From"] = email_sender
            EM["To"] = email_receiver
            EM["Subject"] = subject
            EM.set_content(body)

            context = ssl.create_default_context(cafile=certifi.where())

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, EM.as_string())

            print("SENT")

            return Response({"otp": otp}, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_username(data)
        assert validate_password(data)

        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data["username"]
            password = request.data["password"]
            user = authenticate(username=username, password=password)
            if user:
                token, create = Token.objects.get_or_create(user=user)
                login(request, user)
                user_data = {
                    "username": user.username,
                    "is_admin": user.is_staff,
                }
                return Response(
                    {"token": token.key, "user": user_data}, status=status.HTTP_200_OK
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


UserModel = get_user_model()


class EditUserInformation(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        user = request.user
        # fullname = data["fullname"].strip()
        password = data["password"].strip()
        country = data["country"].strip()
        email = data["email"].strip()
        # cultura_user.fullname = fullname
        cultura_user = CulturaUser.objects.get(user=user)
        # print(user.check_password(password))
        if not user.check_password(password):
            return Response(
                {"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST
            )
        if UserModel.objects.filter(email=email).exists():
            return Response(
                {"error": "Choose another email"}, status=status.HTTP_400_BAD_REQUEST
            )

        user.email = email
        user.save()

        cultura_user.email = email
        cultura_user.country = country
        cultura_user.save()
        return Response(status=status.HTTP_200_OK)


class OTPVerification(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        email = data.get("email", "").strip()
        username = data.get("username", "").strip()

        if not UserModel.objects.filter(email=email) and not UserModel.objects.filter(
            username=username
        ):
            from email.message import EmailMessage
            import ssl
            import smtplib
            import random
            import math
            import certifi

            # generating OTP 6 digit code

            otp = random.randint(100000, 999999)

            print("OTP:", otp)

            # SENDING TO EMAIL
            email_sender = "culturalink62@gmail.com"
            email_password = "syhj wqky hzwz kllz"
            email_receiver = email
            subject = "Verify Your Account - CulturaLink Registration"

            body = (
                "Welcome to Cultura!\n\nTo complete your registration, please enter the following code in your Cultura Application:\n\n\n"
                + str(otp)
                + "\n\n\nif you did not request this please send us an email to this address right away"
            )

            EM = EmailMessage()
            EM["From"] = email_sender
            EM["To"] = email_receiver
            EM["Subject"] = subject
            EM.set_content(body)

            context = ssl.create_default_context(cafile=certifi.where())

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, EM.as_string())

            print("SENT")

            return Response({"otp": otp}, status=status.HTTP_200_OK)
        return Response(
            {
                "email_error": (
                    "This email has already been used in another account"
                    if UserModel.objects.filter(email=email)
                    else None
                ),
                "username_error": (
                    "This username has already been used in another account"
                    if UserModel.objects.filter(username=username)
                    else None
                ),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class EditUserProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        image = request.FILES.get("image", None)
        # print(image)

        cultura_user = CulturaUser.objects.get(user=request.user)
        cultura_user.user_photo = image
        cultura_user.save()

        return Response(status=status.HTTP_200_OK)


import logging

logger = logging.getLogger(__name__)


class UserLogout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        print("logout user: ", user.id)

        if not Survey.objects.filter(user_id=user.id):
            print("Exist")
            return Response(
                {"message": "You have not completed the survey yet."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Retrieve the token from the request headers
        token_key = request.auth.key if request.auth else None
        print("token_key: ", token_key)
        if token_key:
            try:
                token_obj = Token.objects.get(key=token_key)
                token_obj.delete()
            except Token.DoesNotExist:
                return Response(
                    {"message": "Invalid token."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        logout(request)
        return Response(status=status.HTTP_200_OK)


class GetSurvey(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        q1 = data.get("q1", "").strip()
        q2 = data.get("q2", "").strip()
        q3 = data.get("q3", "").strip()
        q4 = data.get("q4", "").strip()
        q5 = data.get("q5", "").strip()
        q6 = data.get("q6", "").strip()

        survey_data = Survey.objects.create(
            user=request.user, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6
        )
        serializer = SurveySerializer(survey_data)

        return Response(serializer.data, status=status.HTTP_200_OK)


from django.contrib.auth import get_user_model

User = get_user_model()


# from .models import ImageModel
class PostCreate(APIView):
    """
    API view for creating and updating Post instances.
    Only authenticated users can create or update posts.
    Session and token authentication are used for security.
    """

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
    )

    def post(self, request):
        """
        Handles the creation of a new Post instance.
        Extracts title, body, and country from the request data.
        Creates a new Post object, serializes it, and returns the serialized data in the response.
        """
        data = request.data

        title = data.get("title", "").strip()
        category = data.get("category", "").strip()
        body = data.get("body", "").strip()
        # imgs = data.get("imgs", "").strip()
        image = request.FILES.get("image", None)
        country = data.get("country", "").strip()
        itinerary_id = data.get("itinerary_id", 0)
        try:
            post = Post(
                author=request.user,
                title=title,
                category=category,
                content=body,
                image=image,
                itinerary=itinerary_id,
                country=country,
            )
            post.save()
        except Exception as e:
            return Response(
                {"error": "An error occurred while creating the post."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        serializer = PostSerializer(post, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, post_id):
        """
        Handles the updating of an existing Post instance.
        Extracts title, body, and image from the request data.
        Updates the Post object, serializes it, and returns the serialized data in the response.
        """
        data = request.data
        object_id = ObjectId(post_id)
        # print("MY OBJ ID ",object_id)
        title = data.get("title", "").strip()
        body = data.get("body", "").strip()
        image = request.FILES.get("image", None)
        try:
            post = Post.objects.get(_id=object_id, author=request.user)
            post.title = title
            post.content = body
            post.image = image
            post.save()
        except Post.DoesNotExist:
            return Response(
                {
                    "error": "Post not found or you do not have permission to edit this post."
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"error": "An error occurred while updating the post."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        serializer = PostSerializer(post, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["post"])
    def like_post(self, request, pk=None):
        object_id = ObjectId(pk)
        post = Post.objects.get(_id=object_id)

        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            message = "post unliked"
            LikeNotification.objects.filter(post_obj_id=object_id).delete()
            user_cult = CulturaUser.objects.get(user=request.user)
            user_cult.like_leader -= 1
            user_cult.save()
        else:
            post.likes.add(user)
            user_cult = CulturaUser.objects.get(user=request.user)
            # print(user_cult.user)
            user_cult.like_leader += 1
            user_cult.save()
            message = "post liked"
            like_notification = LikeNotification(
                post_obj_id=object_id,
                post_author=post.author,
                notif_type="like",
                post_title=post.title,
                post_content=post.content,
                audience=user_cult.user,
            )
            like_notification.save()

            # Optionally, handle unlike action, e.g., delete the notification

        # Serialize the LikeNotification instance

        return Response(status=status.HTTP_200_OK)


class Following(viewsets.ModelViewSet):
    queryset = CulturaUser.objects.all()
    serializer_class = CulturaUserSerializer

    @action(detail=True, methods=["post"])
    def follow(self, request, pk=None):
        user = request.user

        # Ensure pk is an integer
        try:
            user_to_follow = get_object_or_404(CulturaUser, user=pk)
        except ValueError:
            return Response(
                {"error": "Invalid user ID"}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CulturaUserSerializer(
            user_to_follow, context={"request": request}
        )  # pass the request to the serializer

        if user in user_to_follow.followers.all():
            user_to_follow.followers.remove(user)
            FollowingNotification.objects.filter(
                followed_by=user, following=user_to_follow
            ).delete()
            user_to_follow.save()
            message = "User unfollowed"
        else:
            user_to_follow.followers.add(user)
            user_to_follow.save()
            following_notif = FollowingNotification(
                followed_by=user,
                following=user_to_follow,
                notif_type="follow",
            )
            following_notif.save()
            message = "User followed"

        return Response(
            {"message": message, "user": serializer.data}, status=status.HTTP_200_OK
        )  # r


class FollowedNotification(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_data = (
            FollowingNotification.objects.filter(following=request.user.id)
            .exclude(followed_by=request.user)
            .order_by("-created_at")
        )

        # print('Followed: ',follow_serializer.data)

        follow_serializer = FollowSerializer(following_data, many=True)
        for follow_data in follow_serializer.data:
            who_followed = follow_data.get("followed_by")
            if isinstance(who_followed, dict):
                user_id = who_followed.get("id")
            else:
                user_id = who_followed

            username_ = User.objects.get(id=user_id).username
            follow_data["followed_by"] = username_
            user_follow = CulturaUser.objects.filter(user=user_id)
            user_serializer = CulturaUserSerializer(user_follow, many=True)
            for user_data in user_serializer.data:
                image = user_data.get("user_photo", None)
                if image:
                    # Build the absolute URI for the image
                    abs_image_url = request.build_absolute_uri(image)
                    # Update the post data with the absolute URI
                    user_data["user_photo"] = abs_image_url
                if isinstance(user_data["user"], dict):
                    user_id = user_data["user"]["id"]
                else:
                    user_id = user_data["user"]
                username = User.objects.get(id=user_id).username
                user_data["username"] = username
                follow_data["user_data"] = user_serializer.data
        return Response(follow_serializer.data, status=status.HTTP_200_OK)


class LikesNotificationList(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        data = (
            LikeNotification.objects.filter(post_author=request.user)
            .exclude(audience=request.user)
            .order_by("-created_at")
        )

        # following_data = FollowingNotification.objects.filter(following=request.user.id)

        serializer = LikeSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class NotificationStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        notification_type = request.data.get("notification_type")
        notification_id = request.data.get("notification_id")
        is_read = request.data.get("is_read", True)
        print("notif id ", notification_id, "notif type: ", notification_type)
        if notification_type not in ["like", "follow"]:
            return Response(
                {"error": "Invalid notification type"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if notification_type == "like":
            try:
                notification = LikeNotification.objects.get(
                    _id=ObjectId(notification_id), post_author=request.user
                )
            except LikeNotification.DoesNotExist:
                return Response(
                    {"error": "Notification not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            notification.is_read = is_read
            notification.save()
            serializer = LikeSerializer(notification)
        else:  # follow notification
            try:
                notification = FollowingNotification.objects.get(
                    _id=ObjectId(notification_id), following=str(request.user.id)
                )

            except FollowingNotification.DoesNotExist:
                return Response(
                    {"error": "Notification not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            notification.is_read = is_read
            notification.save()
            serializer = FollowSerializer(notification)

        return Response(serializer.data)


class MarkAllNotificationsReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Update all unread like notifications
        LikeNotification.objects.filter(post_author=request.user, is_read=False).update(
            is_read=True
        )

        # Update all unread follow notifications
        FollowingNotification.objects.filter(
            following=str(request.user.id), is_read=False
        ).update(is_read=True)

        return Response(
            {"message": "All notifications marked as read"}, status=status.HTTP_200_OK
        )


class PostListView(APIView):
    """
    API view to retrieve a list of all Post instances from the database.
    Any user, authenticated or not, is allowed to access this view.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={"user": request.user})

        for post_data in serializer.data:
            self.update_image_url(post_data, request)
            self.update_comments(post_data, request)
            self.update_author(post_data)
            self.update_itinerary(post_data, request)
            self.update_cultura_user(post_data, request)
            self.update_likers(post_data, request)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update_image_url(self, post_data, request):
        image = post_data.get("image")
        if image:
            abs_image_url = request.build_absolute_uri(image)
            post_data["image"] = abs_image_url

    def update_comments(self, post_data, request):
        comments = Comment.objects.filter(post_id=post_data["_id"])
        comment_serializer = CommentSerializer(
            comments, many=True, context={"request": request}
        )
        post_data["comments"] = comment_serializer.data

    def update_author(self, post_data):
        post_user = User.objects.get(id=post_data["author"]).username
        post_data["author"] = post_user

    def update_itinerary(self, post_data, request):
        itinerary_id = post_data.get("itinerary")
        if itinerary_id:
            itineraries = SaveItinerary.objects.filter(id=int(itinerary_id))
            itinerary_serializer = SaveItinerarySerializer(
                itineraries, many=True, context={"request": request}
            )
            post_data["itinerary_in_post"] = itinerary_serializer.data

    def update_likers(self, post_data, request):
        likers = post_data.get("likes", [])
        user_ids = [liker["id"] for liker in likers]
        cultura_users = CulturaUser.objects.filter(user_id__in=user_ids)
        cultura_user_serializer = CulturaUserSerializer(
            cultura_users, many=True, context={"request": request}
        )
        post_data["likers"] = cultura_user_serializer.data

    def update_cultura_user(self, post_data, request):
        author_username = post_data["author"]
        user = User.objects.get(username=author_username)
        cultura_user = CulturaUser.objects.get(user=user)
        cultura_user_serializer = CulturaUserSerializer(
            cultura_user, context={"request": request}
        )
        post_data["cultura_user"] = cultura_user_serializer.data


class LikedPostView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, post_id, notif=None):
        post = self.get_post(post_id)
        if notif and self.is_valid_object_id(notif):
            self.mark_notification_as_read(notif)
        serializer = PostSerializer(post, many=True, context={"user": request.user})
        self.update_post_data(serializer.data, request)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_post(self, post_id):
        object_id = ObjectId(post_id)
        return Post.objects.filter(_id=object_id)

    def mark_notification_as_read(self, notif):
        notif_id = ObjectId(notif)
        LikeNotification.objects.filter(_id=notif_id).update(is_read=True)

    def update_likers(self, post_data, request):
        likers = post_data.get("likes", [])
        user_ids = [liker["id"] for liker in likers]
        cultura_users = CulturaUser.objects.filter(user_id__in=user_ids)
        cultura_user_serializer = CulturaUserSerializer(
            cultura_users, many=True, context={"request": request}
        )
        post_data["likers"] = cultura_user_serializer.data

    def is_valid_object_id(self, object_id):
        try:
            ObjectId(object_id)
            return True
        except errors.InvalidId:
            return False

    def update_post_data(self, post_data_list, request):
        for post_data in post_data_list:
            self.update_image_url(post_data, request)
            self.update_comments(post_data, request)
            self.update_author(post_data)
            self.update_itinerary(post_data, request)
            self.update_cultura_user(post_data, request)
            self.update_likers(post_data, request)

    def update_image_url(self, post_data, request):
        image = post_data.get("image")
        if image:
            abs_image_url = request.build_absolute_uri(image)
            post_data["image"] = abs_image_url

    def update_comments(self, post_data, request):
        comments = Comment.objects.filter(post_id=post_data["_id"])
        comment_serializer = CommentSerializer(comments, many=True)
        for comment in comment_serializer.data:
            user = User.objects.get(id=comment["author"])
            cultura_user = CulturaUser.objects.get(user=user)
            cultura_user_serializer = CulturaUserSerializer(
                cultura_user, context={"request": request}
            )
            comment["author"] = cultura_user_serializer.data
        post_data["comments"] = comment_serializer.data

    def update_author(self, post_data):
        post_user = User.objects.get(id=post_data["author"]).username
        post_data["author"] = post_user

    def update_itinerary(self, post_data, request):
        itinerary_id = post_data.get("itinerary")
        if itinerary_id:
            itineraries = SaveItinerary.objects.filter(id=int(itinerary_id))
            itinerary_serializer = SaveItinerarySerializer(itineraries, many=True)
            for itinerary_data in itinerary_serializer.data:
                main_image = itinerary_data.get("main_image")
                if main_image:
                    abs_main_image_url = request.build_absolute_uri(main_image)
                    itinerary_data["main_image"] = abs_main_image_url
            post_data["itinerary_in_post"] = itinerary_serializer.data

    def update_cultura_user(self, post_data, request):
        author_username = post_data["author"]
        user = User.objects.get(username=author_username)
        cultura_user = CulturaUser.objects.get(user=user)
        cultura_user_serializer = CulturaUserSerializer(
            cultura_user, context={"request": request}
        )
        post_data["cultura_user"] = cultura_user_serializer.data


class ProfilePostListView(APIView):
    """
    API view to retrieve a list of all Post instances from the database.
    Any user, authenticated or not, is allowed to access this view.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        posts = Post.objects.filter(author=request.user)

        # Serialize the posts
        serializer = PostSerializer(posts, many=True, context={"user": request.user})
        # Include the image URLs in the response

        for post_data in serializer.data:
            image = post_data.get("image", None)
            if image:
                # Build the absolute URI for the image
                abs_image_url = request.build_absolute_uri(image)
                # Update the post data with the absolute URI
                post_data["image"] = abs_image_url

            # Retrieve comments for the post

            author_user_photo = CulturaUser.objects.get(
                user=post_data["author"]
            ).user_photo
            # Build the absolute URI for the post author's user_photo
            abs_author_user_photo_url = request.build_absolute_uri(
                author_user_photo.url
            )
            # Update the post data with the absolute URI of the post author's user_photo
            post_data["author_user_photo"] = abs_author_user_photo_url
            comments = Comment.objects.filter(post_id=post_data["_id"])

            comment_serializer = CommentSerializer(comments, many=True)
            comment_data = comment_serializer.data
            for comment in comment_data:
                user = User.objects.get(id=comment["author"]).username
                author_user_photo = CulturaUser.objects.get(
                    user=comment["author"]
                ).user_photo

                # Build the absolute URI for each comment author's user_photo
                abs_author_user_photo_url = request.build_absolute_uri(
                    author_user_photo.url
                )
                # Update the comment data with the absolute URI of each comment author's user_photo
                comment["author_user_photo"] = abs_author_user_photo_url
                comment["author"] = user

            post_data["comments"] = comment_data
            post_user = User.objects.get(id=post_data["author"]).username
            post_data["author"] = post_user

            # get-itineraries
            Itinerary_ID = post_data.get("itinerary", 0)
            # print(post_data)
            if Itinerary_ID:
                itineraries = SaveItinerary.objects.filter(id=int(Itinerary_ID))
                IT_serializer = SaveItinerarySerializer(itineraries, many=True)
                # print(IT_serializer)
                for itinerary_data in IT_serializer.data:
                    main_image = itinerary_data.get("main_image", None)
                    if main_image:
                        # Build the absolute URI for the main image
                        abs_main_image_url = request.build_absolute_uri(main_image)
                        # Update the itinerary data with the absolute URI
                        itinerary_data["main_image"] = abs_main_image_url
                    post_data["itinerary_in_post"] = itinerary_data

        following_data = FollowingNotification.objects.filter(following=request.user.id)
        # print('Followed: ',follow_serializer.data)
        follow_serializer = FollowSerializer(
            following_data, many=True, context={"user": request.user}
        )
        # print("USER  NOW", request.user)
        for follow_data in follow_serializer.data:
            who_followed = follow_data.get("followed_by")
            if isinstance(who_followed, dict):
                user_id = who_followed.get("id")
            else:
                user_id = who_followed

            username_ = User.objects.get(id=user_id).username
            follow_data["followed_by"] = username_
            user_follow = CulturaUser.objects.filter(user=user_id)
            user_serializer = CulturaUserSerializer(user_follow, many=True)
            for user_data in user_serializer.data:
                image = user_data.get("user_photo", None)
                if image:
                    # Build the absolute URI for the image
                    abs_image_url = request.build_absolute_uri(image)
                    # Update the post data with the absolute URI
                    user_data["user_photo"] = abs_image_url
                if isinstance(user_data["user"], dict):
                    user_id = user_data["user"]["id"]
                else:
                    user_id = user_data["user"]
                username = User.objects.get(id=user_id).username
                user_data["username"] = username
                follow_data["user_data"] = user_serializer.data

        return Response(
            {"followers": follow_serializer.data, "posts": serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request):

        data = request.data

        post_id = data.get("post_id", "").strip()
        object_id = ObjectId(post_id)
        user = CulturaUser.objects.get(user=request.user)
        user.content_creator += 1
        user.save()
        try:
            post = Post.objects.get(_id=object_id)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CommentCreate(APIView):
    """
    API view to create a new comment for a specific post.
    """

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
    )

    def post(self, request):
        """
        Handle POST request to create a new comment.

        Parameters:
        - request: Request object containing post_id and body

        Returns:
        - Response with serialized comment data
        """
        data = request.data
        post_id = data.get("post_id", "").strip()
        reply = data.get("body", "").strip()
        replied_to = data.get("replied_to", "").strip()
        object_id = ObjectId(post_id)

        user = CulturaUser.objects.get(user=request.user)
        user.comment_connoisseur += 1
        user.save()
        import logging

        comment = Comment.objects.create(
            post_id=post_id,
            author=request.user,
            replied_to=replied_to,
            body=reply,
        )
        post = Post.objects.get(_id=object_id)
        title = post.title

        like_notification = LikeNotification(
            post_obj_id=post_id,
            post_author=replied_to,
            notif_type="commented",
            post_title=title,
            post_content=reply,
            audience=request.user.username,
        )
        like_notification.save()
        logging.info(
            f"Comment created - Post ID: {post_id}, Author: {request.user.username}"
        )

        serializer = CommentSerializer(comment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, comment_id):
        """
        Handle PUT request to update an existing comment.

        Parameters:
        - request: Request object containing the updated body
        - comment_id: ID of the comment to be updated

        Returns:
        - Response with serialized comment data
        """
        comment = get_object_or_404(Comment, _id=ObjectId(comment_id))
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, _id):
        try:
            # Retrieve the comment by _id and owner

            comment = Comment.objects.get(_id=ObjectId(_id), author=request.user)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response(
                {"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND
            )


class CommentListView(APIView):
    """
    API view to retrieve a list of all Post instances from the database.
    Any user, authenticated or not, is allowed to access this view.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        comments = Comment.objects.all()

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteItinerary(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data

        itinerary_id = data.get("id", 0)

        try:
            itinerary = Itinerary.objects.get(id=itinerary_id)
            itinerary.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SaveItinerary.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UpdateSaveItineraryView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        try:
            # Retrieve the itinerary by id and owner
            itinerary_save = SaveItinerary.objects.get(id=id, owner=request.user)
            data = request.data

            if "main_title" in data:
                itinerary_save.main_title = data.get(
                    "main_title", itinerary_save.main_title
                ).strip()
            if "main_description" in data:
                itinerary_save.main_description = data.get(
                    "main_description", itinerary_save.main_description
                ).strip()
            if "gen_tips" in data:
                itinerary_save.gen_tips = data.get(
                    "gen_tips", itinerary_save.gen_tips
                ).strip()
            if "currency" in data:
                itinerary_save.currency = data.get(
                    "currency", itinerary_save.currency
                ).strip()
            if "total_budget" in data:
                itinerary_save.total_budget = data.get(
                    "total_budget", itinerary_save.total_budget
                )
            if "itineraries" in data:
                itinerary_save.itineraries = data.get(
                    "itineraries", itinerary_save.itineraries
                )
            if "image" in request.FILES:
                itinerary_save.main_image = request.FILES.get(
                    "image", itinerary_save.main_image
                )

            itinerary_save.save()
            serializer = SaveItinerarySerializer(itinerary_save)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SaveItinerary.DoesNotExist:
            return Response(
                {"error": "Itinerary not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, id):
        try:
            # Retrieve the itinerary by id and owner
            itinerary = SaveItinerary.objects.get(id=id, owner=request.user)
            itinerary.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SaveItinerary.DoesNotExist:
            return Response(
                {"error": "Itinerary not found"}, status=status.HTTP_404_NOT_FOUND
            )


class ItineraryCreate(APIView):
    """
    API view for creating a new Itinerary instance.
    Only authenticated users can create itineraries.
    Session and token authentication are used for security.
    """

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
    )

    def post(self, request):
        """
        Handles the creation of a new Itinerary instance.
        Extracts title, description, and country from the request data.
        Creates a new Itinerary object, serializes it, and returns the serialized data in the response.
        """
        data = request.data

        longitude = data.get("longitude", 0.0)
        latitude = data.get("latitude", 0.0)

        budget = data.get("budget", 0.0)
        code = data.get("code", "").strip()
        image = request.FILES.get("image", None)
        itinerary = Itinerary.objects.create(
            owner=request.user,
            place_image=image,
            creator_name=request.user.username,
            longitude=longitude,
            latitude=latitude,
            code=code,
            budget=budget,
        )
        # itinerary.save()
        serializer = ItinerarySerializer(itinerary)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        try:
            # Retrieve the itinerary by id and owner
            itinerary = Itinerary.objects.get(id=id, owner=request.user)
            data = request.data

            itinerary.longitude = data.get("longitude", itinerary.longitude)
            itinerary.latitude = data.get("latitude", itinerary.latitude)
            itinerary.budget = data.get("budget", itinerary.budget)
            print(
                "DATA: ",
                data.get(
                    "longitude",
                ),
            )

            itinerary.save()
            serializer = ItinerarySerializer(itinerary)
            print("IT :: ", serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Itinerary.DoesNotExist:
            return Response(
                {"error": "Itinerary not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, id, viewed_it_id=None):
        print("VIEWED ID:: ", viewed_it_id)
        try:
            if viewed_it_id:
                # Retrieve the SaveItinerary by viewed_it_id and owner
                save_itinerary = SaveItinerary.objects.get(
                    id=viewed_it_id, owner=request.user
                )
                itineraries = save_itinerary.itineraries.split(",")
                if str(id) in itineraries:
                    itineraries.remove(str(id))
                    save_itinerary.itineraries = ",".join(itineraries)
                    save_itinerary.save()
                else:
                    return Response(
                        {"error": "Itinerary not found in SaveItinerary"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
            else:
                # Retrieve the itinerary by id and owner
                itinerary = Itinerary.objects.get(id=id, owner=request.user)
                itinerary.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SaveItinerary.DoesNotExist:
            return Response(
                {"error": "SaveItinerary not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Itinerary.DoesNotExist:
            return Response(
                {"error": "Itinerary not found"}, status=status.HTTP_404_NOT_FOUND
            )


import logging
from django.conf import settings
import os
import random
from django.core.mail import send_mail

logger = logging.getLogger(__name__)
User = get_user_model()


class ItineraryListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        itineraries = Itinerary.objects.filter(status="onqueue", owner=request.user)
        serializer = ItinerarySerializer(itineraries, many=True)
        for itinerary_data in serializer.data:
            if main_image := itinerary_data.get("place_image", None):
                # Build the absolute URI for the main image
                abs_main_image_url = request.build_absolute_uri(main_image)
                # Update the itinerary data with the absolute URI
                itinerary_data["place_image"] = abs_main_image_url
        # print(itinerary_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ItinerariesInView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):

        itineraries = Itinerary.objects.filter(id=id)
        serializer = ItinerarySerializer(itineraries, many=True)
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # Your logic to return the itineraries


class UpdateSaveItineraryAndStatus(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, id, id_in_saved_itinerary):
        try:
            # Retrieve the SaveItinerary by id and owner
            save_itinerary = SaveItinerary.objects.get(
                id=id_in_saved_itinerary, owner=request.user
            )
            data = request.data

            # Append or include the id to itineraries
            itineraries = save_itinerary.itineraries.split(",")
            if str(id) not in itineraries:
                itineraries.append(str(id))
            save_itinerary.itineraries = ",".join(itineraries)

            # Find the Itinerary by id and update the status to saved
            itinerary = Itinerary.objects.get(id=id, owner=request.user)
            itinerary.status = "saved"
            itinerary.save()

            save_itinerary.save()
            serializer = SaveItinerarySerializer(save_itinerary)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SaveItinerary.DoesNotExist:
            return Response(
                {"error": "SaveItinerary not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Itinerary.DoesNotExist:
            return Response(
                {"error": "Itinerary not found"}, status=status.HTTP_404_NOT_FOUND
            )


class SaveItineraryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve all itineraries owned by the current user
        itineraries = SaveItinerary.objects.filter(owner=request.user)
        serializer = SaveItinerarySerializer(itineraries, many=True)

        for itinerary_data in serializer.data:
            main_image = itinerary_data.get("main_image", None)
            if main_image:
                # Build the absolute URI for the main image
                abs_main_image_url = request.build_absolute_uri(main_image)
                # Update the itinerary data with the absolute URI
                itinerary_data["main_image"] = abs_main_image_url
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        # Default to None if not provided
        main_title = data.get("main_title", "").strip()
        main_description = data.get("main_description", "").strip()
        gen_tips = data.get("gen_tips", "").strip()
        currency = data.get("currency", "").strip()
        total_budget = data.get("total_budget", 0.0)
        itinerary_ids = data.get("itineraries", [])
        image = request.FILES.get("image", None)
        itineraries = Itinerary.objects.filter(status="onqueue", owner=request.user)
        itineraries.update(status="saved")

        user = CulturaUser.objects.get(user=request.user)
        user.guide_guru += 1
        user.save()

        itinerary_save = SaveItinerary.objects.create(
            owner=request.user,
            creator_name=request.user.username,
            main_title=main_title,
            main_description=main_description,
            gen_tips=gen_tips,
            currency=currency,
            main_image=image,
            total_budget=total_budget,
            itineraries=itinerary_ids,
        )

        serializer = SaveItinerarySerializer(itinerary_save)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        data = request.data
        user_id = data.get("user_id")
        itinerary_id = data.get("itinerary_id")
        new_rating = data.get("rating")

        try:
            itinerary = SaveItinerary.objects.get(id=itinerary_id)
            if not isinstance(itinerary.rating, list):
                itinerary.rating = []

            # Check if the user_id is already in the rating list
            user_exists = any(
                rating["user_id"] == user_id for rating in itinerary.rating
            )

            if not user_exists:
                print("NOT IN RATINGS")
                itinerary.rating.append(data)  # Append the new rating to the list
                itinerary.save()
            else:
                print("IN RATINGS")
            serializer = SaveItinerarySerializer(itinerary)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except SaveItinerary.DoesNotExist:
            return Response(
                {"error": "Itinerary not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except json.JSONDecodeError as e:
            return Response(
                {"error": f"Failed to parse rating: {e}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SaveItineraryListView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # Retrieve all itineraries owned by the current user

        itineraries = SaveItinerary.objects.all()
        serializer = SaveItinerarySerializer(itineraries, many=True)
        users = CulturaUser.objects.filter(user=request.user)
        user_serializer = CulturaUserSerializer(
            users, many=True, context={"user": request.user}
        )

        for itinerary_data in serializer.data:

            main_image = itinerary_data.get("main_image", None)
            if main_image:
                # Build the absolute URI for the main image
                abs_main_image_url = request.build_absolute_uri(main_image)
                # Update the itinerary data with the absolute URI
                itinerary_data["main_image"] = abs_main_image_url
            # Ensure rating_str is a string before calling replace

            for user_data in user_serializer.data:
                image = user_data.get("user_photo", None)
                if image:
                    # Build the absolute URI for the image
                    abs_image_url = request.build_absolute_uri(image)
                    # Update the post data with the absolute URI
                    itinerary_data["user_photo"] = abs_image_url

        return Response(serializer.data, status=status.HTTP_200_OK)


class ViewItinerary(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):

        itineraries = SaveItinerary.objects.filter(id=id)

        serializer = SaveItinerarySerializer(itineraries, many=True)
        itineraries_list = [item["itineraries"] for item in serializer.data]
        itineraries_list_id = [
            int(item) for item in itineraries_list[0].strip("[]").split(",")
        ]

        serialized_itineraries = []

        for itinerary_id in itineraries_list_id:
            try:
                itinerary = Itinerary.objects.get(id=itinerary_id)
                serialized_itinerary = ItinerarySerializer(itinerary).data
                serialized_itineraries.append(serialized_itinerary)
            except Itinerary.DoesNotExist:
                # Handle the case when the itinerary with the given id does not exist
                pass
        serializer.data[0]["itineraries"] = serialized_itineraries
        for itinerary_data in serializer.data:

            main_image = itinerary_data.get("main_image", None)
            if main_image:
                # Build the absolute URI for the main image
                abs_main_image_url = request.build_absolute_uri(main_image)
                # Update the itinerary data with the absolute URI
                itinerary_data["main_image"] = abs_main_image_url
                cultura_user = CulturaUser.objects.filter(user=itinerary_data["owner"])
                profile = CulturaUserSerializer(cultura_user, many=True)

                for post_data in profile.data:
                    image = post_data.get("user_photo", None)
                    if image:
                        # Build the absolute URI for the image
                        abs_image_url = request.build_absolute_uri(image)
                        # Update the post data with the absolute URI
                        itinerary_data["user_photo"] = abs_image_url
            # print(itinerary_data)
            for item in itinerary_data["itineraries"]:
                # print(item)
                place_image = item.get("place_image", None)
                if place_image:
                    # Build the absolute URI for the main image
                    abs_place_image_url = request.build_absolute_uri(place_image)
                    # Update the itinerary data with the absolute URI
                    item["place_image"] = abs_place_image_url
        # serializer.data['itineraries'] = serialized_itineraries
        # print(serializer.data[0]["itineraries"])
        # itiner = Itinerary.objects.filter(id=itinerary_ids)
        # serializer.data['itineraries'] = ItinerarySerializer(itiner, many=True).data
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetSettings(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data

        in_app_notif = data.get("in_app_notif")
        banner_notif = data.get("banner_notif")
        vibration = data.get("vibration")
        sound = data.get("sound")
        theme = data.get("theme")

        settings = UserSetting.objects.filter(user=request.user)
        settings.update(
            in_app_notification=in_app_notif,
            banner_notification=banner_notif,
            vibration=vibration,
            sound=sound,
            theme=theme,
        )

        serializer = SettingSerializer(settings)

        return Response(serializer.data, status=status.HTTP_200_OK)

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        settings = UserSetting.objects.filter(user=request.user)
        user = CulturaUser.objects.filter(user=request.user)
        user_information = CulturaUserSerializer(user, many=True)
        serializer = SettingSerializer(settings, many=True)
        # print("where ::", serializer.data)
        return Response(
            {"user_information": user_information.data, "set": serializer.data},
            status=status.HTTP_200_OK,
        )


class PublicPostProfile(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.data
        user = request.GET.get("user_id", 0)
        print("user-id: ", user)

        posts = Post.objects.filter(author_id=int(user))

        # Serialize the posts
        serializer = PostSerializer(posts, many=True, context={"user": request.user})
        # Include the image URLs in the response

        for post_data in serializer.data:
            image = post_data.get("image", None)
            if image:
                # Build the absolute URI for the image
                abs_image_url = request.build_absolute_uri(image)
                # Update the post data with the absolute URI
                post_data["image"] = abs_image_url

            # Retrieve comments for the post

            author_user_photo = CulturaUser.objects.get(
                user=post_data["author"]
            ).user_photo
            # Build the absolute URI for the post author's user_photo
            abs_author_user_photo_url = request.build_absolute_uri(
                author_user_photo.url
            )
            # Update the post data with the absolute URI of the post author's user_photo
            post_data["author_user_photo"] = abs_author_user_photo_url
            comments = Comment.objects.filter(post_id=post_data["_id"])

            comment_serializer = CommentSerializer(comments, many=True)
            comment_data = comment_serializer.data
            for comment in comment_data:
                user = User.objects.get(id=comment["author"]).username
                author_user_photo = CulturaUser.objects.get(
                    user=comment["author"]
                ).user_photo

                # Build the absolute URI for each comment author's user_photo
                abs_author_user_photo_url = request.build_absolute_uri(
                    author_user_photo.url
                )
                # Update the comment data with the absolute URI of each comment author's user_photo
                comment["author_user_photo"] = abs_author_user_photo_url
                comment["author"] = user

            post_data["comments"] = comment_data
            post_user = User.objects.get(id=post_data["author"]).username
            post_data["author"] = post_user

            # get-itineraries
            Itinerary_ID = post_data.get("itinerary", 0)
            # print(post_data)
            if Itinerary_ID:
                itineraries = SaveItinerary.objects.filter(id=int(Itinerary_ID))
                IT_serializer = SaveItinerarySerializer(itineraries, many=True)
                # print(IT_serializer)
                for itinerary_data in IT_serializer.data:
                    main_image = itinerary_data.get("main_image", None)
                    if main_image:
                        # Build the absolute URI for the main image
                        abs_main_image_url = request.build_absolute_uri(main_image)
                        # Update the itinerary data with the absolute URI
                        itinerary_data["main_image"] = abs_main_image_url
                    post_data["itinerary_in_post"] = itinerary_data

        # Return the modified serialized data in the response
        return Response(serializer.data, status=status.HTTP_200_OK)


##Searching

from functools import reduce
from django.db.models import Q


class SearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = request.GET.get("title", "").strip()
        if not query:
            return Response({"error": "Search query is missing"}, status=400)

        search_words = query.split()
        if not search_words:
            return Response({})

        q = Q()
        for word in search_words:
            q |= Q(fullname__icontains=word)
        users = CulturaUser.objects.filter(q).exclude(user=request.user)

        q = Q()
        for word in search_words:
            q |= Q(main_title__icontains=word)
        save_itineraries = SaveItinerary.objects.filter(q)

        q = Q()
        for word in search_words:
            q |= (
                Q(title__icontains=word)
                | Q(category__icontains=word)
                | Q(country__icontains=word)
                | Q(content__icontains=word)
            )
        posts = Post.objects.filter(q)

        q = Q()
        for word in search_words:
            q |= Q(post_title__icontains=word)
        notifications = LikeNotification.objects.filter(q)

        user_serializer = CulturaUserSerializer(
            users, many=True, context={"user": request.user}
        )
        for user_data in user_serializer.data:
            image = user_data.get("user_photo", None)
            if image:
                abs_image_url = request.build_absolute_uri(image)
                user_data["user_photo"] = abs_image_url

            user_id = user_data["user"]["id"]
            username = User.objects.get(id=user_id).username
            user_data["username"] = username

        save_itinerary_serializer = SaveItinerarySerializer(save_itineraries, many=True)

        post_serializer = PostSerializer(posts, many=True)

        for post_data in post_serializer.data:
            image = post_data.get("image", None)
            if image:
                abs_image_url = request.build_absolute_uri(image)
                post_data["image"] = abs_image_url

            author_user_photo = CulturaUser.objects.get(
                user=post_data["author"]
            ).user_photo
            abs_author_user_photo_url = request.build_absolute_uri(
                author_user_photo.url
            )
            post_data["author_user_photo"] = abs_author_user_photo_url

            comments = Comment.objects.filter(post_id=post_data["_id"])
            comment_serializer = CommentSerializer(
                comments, many=True, context={"request": request}
            )
            comment_data = comment_serializer.data

            for comment in comment_data:
                user = User.objects.get(id=comment["author"]).username
                author_user_photo = CulturaUser.objects.get(
                    user=comment["author"]
                ).user_photo
                abs_author_user_photo_url = request.build_absolute_uri(
                    author_user_photo.url
                )
                comment["author_user_photo"] = abs_author_user_photo_url
                comment["author"] = user

            post_data["comments"] = comment_data
            post_user = User.objects.get(id=post_data["author"]).username
            post_data["author"] = post_user

            Itinerary_ID = post_data.get("itinerary", 0)
            if Itinerary_ID:
                itineraries = SaveItinerary.objects.filter(id=int(Itinerary_ID))
                IT_serializer = SaveItinerarySerializer(itineraries, many=True)

                for itinerary_data in IT_serializer.data:
                    main_image = itinerary_data.get("main_image", None)
                    if main_image:
                        abs_main_image_url = request.build_absolute_uri(main_image)
                        itinerary_data["main_image"] = abs_main_image_url
                    post_data["itinerary_in_post"] = itinerary_data

            self.update_likers(post_data, request)
            self.update_cultura_user(post_data, request)

        return Response(
            {
                "users": user_serializer.data,
                "save_itineraries": save_itinerary_serializer.data,
                "posts": post_serializer.data,
            }
        )

    def update_likers(self, post_data, request):
        likers = post_data.get("likes", [])
        user_ids = [liker["id"] for liker in likers]
        cultura_users = CulturaUser.objects.filter(user_id__in=user_ids)
        cultura_user_serializer = CulturaUserSerializer(
            cultura_users, many=True, context={"request": request}
        )
        post_data["likers"] = cultura_user_serializer.data

    def update_cultura_user(self, post_data, request):
        author_username = post_data["author"]
        user = User.objects.get(username=author_username)
        cultura_user = CulturaUser.objects.get(user=user)
        cultura_user_serializer = CulturaUserSerializer(
            cultura_user, context={"request": request}
        )
        post_data["cultura_user"] = cultura_user_serializer.data
