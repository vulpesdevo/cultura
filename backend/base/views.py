from gc import get_objects
import json
from django.contrib.auth import get_user_model, login, logout
from django.http import Http404, HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import (
    CulturaUserSerializer,
    ItinerarySerializer,
    LikeSerializer,
    SaveItinerarySerializer,
    UserRegisterSerializer,
    UserLoginSerializer,
    UserSerializer,
    PostSerializer,
    CommentSerializer,
)
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status,viewsets
from .validations import custom_validation, validate_username, validate_password
from .models import Itinerary, LikeNotification, Post, Comment, CulturaUser, SaveItinerary


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
        from django.core import serializers

        UserView.token_auth = str(authorization_header).replace("Token", "").strip()
        serializer = UserSerializer(request.user)
        # cultura_user = CulturaUser.objects.get(user=request.user)
        # cultura_users = CulturaUser.objects.filter(user=request.user)
        cult_user_name = "cultura_users.fullname"
        cultura_user = CulturaUser.objects.get(user=request.user)
        profile = CulturaUserSerializer(cultura_user)
        return Response({"user": serializer.data, "userfullname": cult_user_name,"profile":profile.data}, status=status.HTTP_200_OK)


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
        image = request.FILES.get('image', None)
        country = data.get("country", "").strip()
        print("image: ", image) 
        try:
            post = Post(
            author=request.user,
            title=title,
            category=category,
            content=body,
            image=image,
            country=country,
            )
            post.save()
        except Exception as e:
            return Response(
                {"error": "An error occurred while creating the post."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        serializer = PostSerializer(post,context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
from bson import ObjectId    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def like_post(self, request, pk=None):
        object_id = ObjectId(pk)
        post = Post.objects.get(_id=object_id)
        
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
            message = 'post unliked'
            LikeNotification.objects.filter(post_obj_id=post).delete()
        else:
            post.likes.add(user)

            message = 'post liked'
            like_notification = LikeNotification(
                post_obj_id=post,
                post_author = post.author,
                
                post_title = post.title,
                post_content = post.content,
                liker=user.username,
            )
            like_notification.save()
            
            # Optionally, handle unlike action, e.g., delete the notification
            

        # Serialize the LikeNotification instance
        
        return Response(
                status=status.HTTP_200_OK)


class LikesNotificationList(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        data = LikeNotification.objects.filter(post_author=request.user).order_by('-created_at')
        
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
        print(request.user)
        # Serialize the posts
        serializer = PostSerializer(posts, many=True,context={'user': request.user})
        # Include the image URLs in the response
        for post_data in serializer.data:
            image = post_data.get('image', None)
            if image:
                # Build the absolute URI for the image
                abs_image_url = request.build_absolute_uri(image)
                # Update the post data with the absolute URI
                post_data['image'] = abs_image_url
        
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
        serializer = PostSerializer(posts, many=True,context={'user': request.user} )
        # Include the image URLs in the response
    
        for post_data in serializer.data:
            image = post_data.get('image', None)
            if image:
                # Build the absolute URI for the image
                abs_image_url = request.build_absolute_uri(image)
                # Update the post data with the absolute URI
                post_data['image'] = abs_image_url
        
        # Return the modified serialized data in the response
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

        
        itinerary = Itinerary.objects.create(
            owner=request.user,
            creator_name=request.user.username,
            title=title, 
            longitude=longitude,
            latitude=latitude,
            place_name=place_name,
            description=description,
            budget=budget,
        )
        
        serializer = ItinerarySerializer(itinerary)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

import logging

logger = logging.getLogger(__name__)

class ItineraryListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        
        itineraries = Itinerary.objects.filter(status="onqueue",owner=request.user)
        serializer = ItinerarySerializer(itineraries,many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
class ItinerariesInView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,id):
        
        itineraries = Itinerary.objects.filter(id=id)
        serializer = ItinerarySerializer(itineraries,many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
            # Your logic to return the itineraries
class SaveItineraryView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        # Default to None if not provided
        main_title = data.get('main_title', "").strip()
        main_description = data.get('main_description', "").strip()
        gen_tips = data.get('gen_tips', "").strip()
        currency = data.get('currency', "").strip()
        total_budget = data.get('total_budget', 0.0)
        itinerary_ids = data.get('itineraries', [])
        image = request.FILES.get('image', None)
        itineraries = Itinerary.objects.filter(status="onqueue",owner=request.user)
        itineraries.update(status='saved')
        
        itinerary_save = SaveItinerary.objects.create(
            
            owner=request.user,
            creator_name=request.user.username,
            main_title= main_title,
            main_description= main_description,
            gen_tips= gen_tips,
            currency=currency,
            main_image=image,
            total_budget= total_budget,
            itineraries= itinerary_ids,
            
        )
        
        
        serializer = SaveItinerarySerializer(itinerary_save)
            # Set the owner to the current user before saving
        # itineraries_init = Itinerary.objects.filter(owner=request.user,status=False)
        # for itinerary in itineraries_init:
        #     itinerary.status = True
        #     itinerary.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    

class SaveItineraryListView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Retrieve all itineraries owned by the current user
     
        itineraries = SaveItinerary.objects.filter(owner=request.user)
        serializer = SaveItinerarySerializer(itineraries, many=True)
        
        for itinerary_data in serializer.data:
            main_image = itinerary_data.get('main_image', None)
            if main_image:
                # Build the absolute URI for the main image
                abs_main_image_url = request.build_absolute_uri(main_image)
                # Update the itinerary data with the absolute URI
                itinerary_data['main_image'] = abs_main_image_url
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ViewItinerary(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id):
     
        itineraries = SaveItinerary.objects.filter(id=id)
        
        serializer = SaveItinerarySerializer(itineraries, many=True)
        itineraries_list = [item['itineraries'] for item in serializer.data]
        itineraries_list_id = [int(item) for item in itineraries_list[0].strip('[]').split(',')]
        
        serialized_itineraries = []
        
        
        
        for itinerary_id in itineraries_list_id:
            try:
                itinerary = Itinerary.objects.get(id=itinerary_id)
                serialized_itinerary = ItinerarySerializer(itinerary).data
                serialized_itineraries.append(serialized_itinerary)
            except Itinerary.DoesNotExist:
                # Handle the case when the itinerary with the given id does not exist
                pass
        serializer.data[0]['itineraries'] = serialized_itineraries
        for itinerary_data in serializer.data:
            main_image = itinerary_data.get('main_image', None)
            if main_image:
                # Build the absolute URI for the main image
                abs_main_image_url = request.build_absolute_uri(main_image)
                # Update the itinerary data with the absolute URI
                itinerary_data['main_image'] = abs_main_image_url
        # serializer.data['itineraries'] = serialized_itineraries
        print(serializer.data[0]['itineraries'])
        # itiner = Itinerary.objects.filter(id=itinerary_ids)
        # serializer.data['itineraries'] = ItinerarySerializer(itiner, many=True).data
        return Response(serializer.data, status=status.HTTP_200_OK)