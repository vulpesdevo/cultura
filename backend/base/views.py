from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
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
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status
from .validations import custom_validation, validate_username, validate_password
from .models import Post, Comment, CulturaUser


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
        print("Header Auth: ", authorization_header)

        UserView.token_auth = str(authorization_header).replace("Token", "").strip()
        serializer = UserSerializer(request.user)

        return Response({"user": serializer.data}, status=status.HTTP_200_OK)


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
            token, create = Token.objects.get_or_create(user=user)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(
                {"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK
            )


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
        body = data.get("body", "").strip()
        country = data.get("country", "").strip()

        try:
            post = Post.objects.create(
                
                author=request.user,
                title=title,
                content=body,
                country=country,
            )
        except Exception as e:
            return Response(
                {"error": "An error occurred while creating the post."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def put(self, request):
    #     """
    #     Handles adding a comment to an existing Post instance.
    #     Extracts the post ID and comment body from the request data.
    #     Creates a new Comment object, associates it with the specified post,
    #     serializes the comment, and returns the serialized data in the response.
    #     """

    #     data = request.data
    #     post_id = data.get("post_id", "").strip()
    #     reply = data.get("body", "").strip()
    #     post = Post.objects.get(_id=post_id)

    #     comment = Comment.objects.create(
    #         user_id=request.user, author=post.user, body=reply
    #     )

    #     post.add_comment(comment)

    #     serializer = CommentSerializer(comment)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostListView(APIView):
    """
    API view to retrieve a list of all Post instances from the database.
    Any user, authenticated or not, is allowed to access this view.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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

        import logging

        comment = Comment.objects.create(
            post_id=post_id, 
            author=request.user, 
            replied_to= replied_to,
            body=reply,
        )
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
