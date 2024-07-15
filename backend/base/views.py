from gc import get_objects
import json
from django.contrib.auth import get_user_model, login, logout
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
    UserRegisterSerializer,
    UserLoginSerializer,
    UserSerializer,
    PostSerializer,
    CommentSerializer,
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
    SaveItinerary,
    UserSetting,
)

from profanity.validators import validate_is_profane


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
    )

    ##
    def get(self, request):
        authorization_header = request.headers.get("Authorization")
        # Print the Authorization header value
        # print("Header Auth: ", authorization_header)
        from django.core import serializers

        UserView.token_auth = str(authorization_header).replace("Token", "").strip()
        serializer = UserSerializer(request.user)
        # cultura_user = CulturaUser.objects.get(user=request.user)
        # cultura_users = CulturaUser.objects.filter(user=request.user)
        cult_user_name = "cultura_users.fullname"
        cultura_user = CulturaUser.objects.filter(user=request.user)
        profile = CulturaUserSerializer(cultura_user, many=True)

        for post_data in profile.data:
            image = post_data.get("user_photo", None)
            if image:
                # Build the absolute URI for the image
                abs_image_url = request.build_absolute_uri(image)
                # Update the post data with the absolute URI
                post_data["user_photo"] = abs_image_url

        return Response(
            {
                "user": serializer.data,
                "userfullname": cult_user_name,
                "profile": profile.data,
            },
            status=status.HTTP_200_OK,
        )


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
            # username = serializer.validated_data["username"]
            # password = serializer.validated_data["password"]
            user = serializer.check_user(data)
            # User is already authenticated, return appropriate response
            login(request, user)
            token, create = Token.objects.get_or_create(user=user)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(
                {"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK
            )


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


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):

        get_token = UserView.token_auth
        # print("Logout Token: ", get_token.replace("Token", "").strip())
        del_token = Token.objects.get(key=get_token)
        del_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)


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
        itinerary_id = data.get("itinerary_id", 0).strip()
        # print("image: ", image)
        # Check for profanity in title and body
        # try:
        #     if validate_is_profane(title) or validate_is_profane(body):
        #         raise ValidationError(["Please remove any profanity/swear words."])
        # except ValidationError as e:
        #     return Response(
        #         {
        #             "error": e.messages,
        #             "field": "title" if "title" in e.messages[0] else "body",
        #         },
        #         status=400,
        #     )

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


from bson import ObjectId


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["post"])
    def like_post(self, request, pk=None):
        object_id = ObjectId(pk)
        post = Post.objects.get(_id=object_id)

        user = request.user
        print(post.likes.all())
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
    def follow(self, request, pk):
        print(pk)
        user = request.user

        user_to_follow = CulturaUser.objects.get(user=pk)
        serializer = CulturaUserSerializer(
            user_to_follow, context={"user": self.request.user}
        )  # pass the request to the serializer

        print("user that followed: ", user_to_follow.id)
        if user in user_to_follow.followers.all():
            user_to_follow.followers.remove(user)
            FollowingNotification.objects.filter(
                followed_by=user, following=pk
            ).delete()
            user_to_follow.save()

            message = "User unfollowed"
        else:
            user_to_follow.followers.add(user)

            user_to_follow.save()
            following_notif = FollowingNotification(
                followed_by=user,
                following=pk,
                notif_type="follow",
            )
            following_notif.save()
            message = "User followed"

        return Response(
            serializer.data, status=status.HTTP_200_OK
        )  # return the serialized data


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
            username_ = User.objects.get(id=follow_data["followed_by"]).username
            follow_data["followed_by"] = username_
            user_follow = CulturaUser.objects.filter(user=who_followed)
            # print(user_follow)
            user_serializer = CulturaUserSerializer(user_follow, many=True)
            print(user_serializer.data)
            for user_data in user_serializer.data:
                image = user_data.get("user_photo", None)
                if image:
                    # Build the absolute URI for the image
                    abs_image_url = request.build_absolute_uri(image)
                    # Update the post data with the absolute URI
                    user_data["user_photo"] = abs_image_url
                username = User.objects.get(id=user_data["user"]).username
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


class PostListView(APIView):
    """
    API view to retrieve a list of all Post instances from the database.
    Any user, authenticated or not, is allowed to access this view.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        posts = Post.objects.all()
        # print(request.user)
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

            # Get the user_photo of the post author

            # Get the user_photo of each comment author

            # Validate if the post title is profane
            # title_is_profane = validate_is_profane(title)

            # print(title_is_profane)
            # post_data['title'] = "****" if title_is_profane else title
            # Add the profanity flag to the post data

        return Response(serializer.data, status=status.HTTP_200_OK)


class LikedPostView(APIView):
    """
    API view to retrieve a list of all Post instances from the database.
    Any user, authenticated or not, is allowed to access this view.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, post_id, notif):

        object_id = ObjectId(post_id)
        post = Post.objects.filter(_id=object_id)
        serializer = PostSerializer(post, many=True, context={"user": request.user})

        # Serialize the posts
        data = request.data

        notif_id = ObjectId(notif)
        # print("NOTIFICATION ID :: ", notif)
        LikeNotification.objects.filter(_id=notif_id).update(is_read=True)
        # Include the image URLs in the response
        for post_data in serializer.data:
            image = post_data.get("image", None)
            if image:
                # Build the absolute URI for the image
                abs_image_url = request.build_absolute_uri(image)
                # Update the post data with the absolute URI
                post_data["image"] = abs_image_url
            comments = Comment.objects.filter(post_id=post_data["_id"])
            comment_serializer = CommentSerializer(comments, many=True)
            comment_data = comment_serializer.data
            for comment in comment_data:
                user = User.objects.get(id=comment["author"]).username
                comment["author"] = user
            post_data["comments"] = comment_serializer.data
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

        return Response(serializer.data, status=status.HTTP_200_OK)


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

        # Return the modified serialized data in the response
        return Response(serializer.data, status=status.HTTP_200_OK)

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
        title = data.get("title", "").strip()
        place_name = data.get("place_name", "").strip()

        description = data.get("description", "").strip()
        budget = data.get("budget", 0.0)
        code = data.get("code", "").strip()

        itinerary = Itinerary.objects.create(
            owner=request.user,
            creator_name=request.user.username,
            title=title,
            longitude=longitude,
            latitude=latitude,
            place_name=place_name,
            code=code,
            description=description,
            budget=budget,
        )

        serializer = ItinerarySerializer(itinerary)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


import logging
from django.conf import settings
import os
import random
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


class ItineraryListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        itineraries = Itinerary.objects.filter(status="onqueue", owner=request.user)
        serializer = ItinerarySerializer(itineraries, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ItinerariesInView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):

        itineraries = Itinerary.objects.filter(id=id)
        serializer = ItinerarySerializer(itineraries, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        # Your logic to return the itineraries


class SaveItineraryView(APIView):
    permission_classes = [IsAuthenticated]

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
        # Set the owner to the current user before saving
        # itineraries_init = Itinerary.objects.filter(owner=request.user,status=False)
        # for itinerary in itineraries_init:
        #     itinerary.status = True
        #     itinerary.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SaveItineraryListView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # Retrieve all itineraries owned by the current user

        itineraries = SaveItinerary.objects.all()
        serializer = SaveItinerarySerializer(itineraries, many=True)

        for itinerary_data in serializer.data:
            main_image = itinerary_data.get("main_image", None)
            if main_image:
                # Build the absolute URI for the main image
                abs_main_image_url = request.build_absolute_uri(main_image)
                # Update the itinerary data with the absolute URI
                itinerary_data["main_image"] = abs_main_image_url
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
        user = request.GET.get("user_id", "").strip()
        print("user-id: ", user)

        posts = Post.objects.filter(author=user)

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
        data = request.data

        # logging.debug('Request GET: %s', request.GET)
        print("data", data)
        query = request.GET.get("title", "").strip()
        print("INPUT ", query)
        if query is None:  # Check if query is None
            # Return an error response or a default response if search query is missing
            return Response({"error": "Search query is missing"}, status=400)
        search_words = query.split()

        # Use Q objects to create a dynamic filter query

        if not search_words:  # Check if search_words is empty
            # Return an empty response or a default response if search query is empty
            return Response({})

        # Use Q objects to create a dynamic filter query
        q = Q()
        for word in search_words:
            q |= Q(fullname__icontains=word)
        users = CulturaUser.objects.filter(q).exclude(user=request.user)

        q = Q()
        for word in search_words:
            q |= Q(main_title__icontains=word)
        save_itineraries = SaveItinerary.objects.filter(q)

        # q = Q()
        # for word in search_words:
        #     q |= Q(title__icontains=word)
        # itineraries = Itinerary.objects.filter(q)

        # q = Q()
        # for word in search_words:
        #     q |= Q(body__icontains=word)
        # comments = Comment.objects.filter(q)

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
                # Build the absolute URI for the image
                abs_image_url = request.build_absolute_uri(image)
                # Update the post data with the absolute URI
                user_data["user_photo"] = abs_image_url
            username = User.objects.get(id=user_data["user"]).username
            user_data["username"] = username
            # user_id = User.objects.get(id=user_data["user"])
            # post_ = Post.objects.get(author=user_data["user"])._id
            # posts = Post.objects.filter(author=user_data['user'])
            # print(posts)
            # user_data["post_id"] = [post['_id'] for post in posts]

        save_itinerary_serializer = SaveItinerarySerializer(save_itineraries, many=True)
        # itinerary_serializer = ItinerarySerializer(itineraries, many=True)
        # comment_serializer = CommentSerializer(comments, many=True)

        post_serializer = PostSerializer(posts, many=True)

        for post_data in post_serializer.data:
            image = post_data.get("image", None)
            if image:
                # Build the absolute URI for the image
                abs_image_url = request.build_absolute_uri(image)
                # Update the post data with the absolute URI
                post_data["image"] = abs_image_url
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
            # Retrieve comments for the post
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
            if Itinerary_ID:
                itineraries = SaveItinerary.objects.filter(id=int(Itinerary_ID))
                IT_serializer = SaveItinerarySerializer(itineraries, many=True)

                for itinerary_data in IT_serializer.data:
                    main_image = itinerary_data.get("main_image", None)
                    if main_image:
                        # Build the absolute URI for the main image
                        abs_main_image_url = request.build_absolute_uri(main_image)
                        # Update the itinerary data with the absolute URI
                        itinerary_data["main_image"] = abs_main_image_url

                post_data["itinerary_in_post"] = itinerary_data

        return Response(
            {
                "users": user_serializer.data,
                "save_itineraries": save_itinerary_serializer.data,
                # "itineraries": itinerary_serializer.data,
                "posts": post_serializer.data,
            }
        )
