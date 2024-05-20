from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserSerializer,
    PostSerializer,
    CommentSerializer,
)
from rest_framework import permissions, status
from .validations import custom_validation, validate_username, validate_password
from .models import CulturaUser, Post, Comment


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    ##
    def get(self, request):

        serializer = UserSerializer(request.user)

        return Response({"user": serializer.data}, status=status.HTTP_200_OK)


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data

        first_name = data["first_name"].strip()
        last_name = data["last_name"].strip()
        location = data["location"].strip()
        contact = data["contact"].strip()
        email = data["email"].strip()

        email = data["email"].strip()
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            if user := serializer.create(clean_data):
                CulturaUser.objects.create(
                    id=user,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    contact=contact,
                    location=location,
                    #  # Assuming you want to associate the GuestProfile with the created user
                )
                login(request, user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                # return Response({"user": serializer.data})
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
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"user": serializer.data})


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


from django.contrib.auth import get_user_model

User = get_user_model()


class PostCreate(APIView):
    def post(self, request, *args, **kwargs):
        # Create the Post instance with comments set to null
        post = Post.objects.create(
            comments=None,
            author=request.user,
            title=request.data.get("title"),
            body=request.data.get("body"),
        )
        # Serialize the Post instance
        serializer = PostSerializer(post)
        # Return a JSON response
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        # Get the Post instance
        post_id = request.data.get("post_id")
        post = Post.objects.get(_id=post_id)

        # Create the Comment instance
        comment = Comment.objects.create(
            author=request.user, body=request.data.get("body")
        )

        # Add the Comment to the Post
        post.add_comment(comment)

        # Serialize the Comment instance
        serializer = CommentSerializer(comment)

        # Return a JSON response
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentCreate(APIView):
    def post(self, request):
        # Get the Post instance
        post_id = request.data.get("post_id")
        post = Post.objects.get(id=post_id)

        # Create the Comment instance
        comment = Comment.objects.create(
            post=post, 
            author=request.user, 
            body=request.data.get("body")
        )

        # Serialize the Comment instance
        serializer = CommentSerializer(comment)

        # Return a JSON response
        return Response(serializer.data, status=status.HTTP_201_CREATED)
