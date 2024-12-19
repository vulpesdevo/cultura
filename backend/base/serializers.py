from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import (
    FollowingNotification,
    LikeNotification,
    Post,
    Comment,
    CulturaUser,
    Itinerary,
    SaveItinerary,
    Survey,
    UserSetting,
    Report,
)
from bson import ObjectId

from djongo import models

UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, clean_data):

        user_obj = UserModel.objects.create_user(
            username=clean_data["username"],
            password=clean_data["password"],
        )

        user_obj.fullname = clean_data["fullname"]
        user_obj.email = clean_data["email"]
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    is_admin = serializers.SerializerMethodField()

    def get_is_admin(self, obj):
        user = CulturaUser.objects.get(username=obj["username"])
        return user.is_staff

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            return {
                "username": user.username,
                "is_admin": user.is_staff,
            }
        raise serializers.ValidationError("Invalid credentials")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = [
            "id",
            "username",
            "email",
        ]


class CulturaUserSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only=True)
    follow_count = serializers.SerializerMethodField()
    is_followed = serializers.SerializerMethodField()
    user = UserSerializer()
    posts = serializers.SerializerMethodField()

    class Meta:
        model = CulturaUser
        fields = "__all__"

    def get_follow_count(self, obj):
        return len(obj.followers.all())

    def get_is_followed(self, obj):
        user = self.context.get("user")
        print("USER : ", user)
        return True if user in obj.followers.all() else False

    def get_user_photo(self, obj):
        request = self.context.get("request")
        if obj.user_photo and request:
            return request.build_absolute_uri(obj.user_photo.url)
        return None

    def get_posts(self, obj):
        if hasattr(obj, "user") and obj.user:
            try:
                posts = Post.objects.filter(author=obj.user)
                return PostSerializer(posts, many=True).data
            except User.DoesNotExist:
                return []
        return []


class SearchResultUserSerializer(serializers.ModelSerializer):
    user_photo = serializers.SerializerMethodField()

    class Meta:
        model = CulturaUser
        fields = "__all__"

    def get_user_photo(self, obj):
        request = self.context.get("request")
        if obj.user_photo and request:
            return request.build_absolute_uri(obj.user_photo.url)
        return None


class SearchResultSaveItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveItinerary
        fields = "__all__"


class SearchResultPostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    author_user_photo = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    itinerary_in_post = serializers.SerializerMethodField()
    cultura_user = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    likers = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "_id",
            "author",
            "title",
            "content",
            "category",
            "image",
            "author_user_photo",
            "country",
            "date_posted",
            "likes",
            "likers",
            "itinerary",
            "like_count",
            "is_liked",
            "comments",
            "itinerary_in_post",
            "cultura_user",
        ]

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_author_user_photo(self, obj):
        try:
            author_user_photo = CulturaUser.objects.get(user=obj.author).user_photo
            request = self.context.get("request")
            if author_user_photo and request:
                return request.build_absolute_uri(author_user_photo.url)
        except ObjectDoesNotExist:
            return None

    def get_comments(self, obj):
        comments = Comment.objects.filter(post_id=obj._id)
        request = self.context.get("request")
        comment_serializer = CommentSerializer(
            comments, many=True, context={"request": request}
        )
        return comment_serializer.data

    def get_itinerary_in_post(self, obj):
        itinerary_id = obj.itinerary
        if itinerary_id:
            itineraries = SaveItinerary.objects.filter(id=int(itinerary_id))
            request = self.context.get("request")
            itinerary_serializer = SaveItinerarySerializer(
                itineraries, many=True, context={"request": request}
            )
            for itinerary_data in itinerary_serializer.data:
                main_image = itinerary_data.get("main_image", None)
                if main_image:
                    abs_main_image_url = request.build_absolute_uri(main_image)
                    itinerary_data["main_image"] = abs_main_image_url
            return itinerary_serializer.data
        return []

    def get_cultura_user(self, obj):
        try:
            user = UserModel.objects.get(id=obj.author.id)
            cultura_user = CulturaUser.objects.get(user=user)
            request = self.context.get("request")
            cultura_user_serializer = CulturaUserSerializer(
                cultura_user, context={"request": request}
            )
            return cultura_user_serializer.data
        except ObjectDoesNotExist:
            return None

    def get_like_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        user = self.context.get("user")
        return user in obj.likes.all()

    def get_likers(self, obj):
        likers = obj.likes.all()
        user_ids = [liker.id for liker in likers]
        cultura_users = CulturaUser.objects.filter(user_id__in=user_ids)
        request = self.context.get("request")
        cultura_user_serializer = CulturaUserSerializer(
            cultura_users, many=True, context={"request": request}
        )
        return cultura_user_serializer.data


class SearchResultCommentSerializer(serializers.ModelSerializer):
    author_user_photo = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "content", "author", "author_user_photo"]

    def get_author_user_photo(self, obj):
        try:
            author_user_photo = CulturaUser.objects.get(user=obj.author).user_photo
            request = self.context.get("request")
            if author_user_photo and request:
                return request.build_absolute_uri(author_user_photo.url)
        except ObjectDoesNotExist:
            return None


class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = FollowingNotification
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = LikeNotification
        fields = (
            "_id",
            "post_obj_id",
            "notif_type",
            "post_author",
            "post_title",
            "post_content",
            "audience",
            "is_read",
            "created_at",
        )


class PostSerializer(serializers.ModelSerializer):

    likes = UserSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    # date_get_like = serializers.SerializerMethodField()
    # comment_count = serializers.SerializerMethodField()
    # date_get_like = serializers.DateTimeField(auto_now_add=True)
    class Meta:
        model = Post
        fields = (
            "_id",
            "author",
            "title",
            "content",
            "category",
            "image",
            "country",
            "date_posted",
            "likes",
            "itinerary",
            "like_count",
            "is_liked",
            "comments",
        )

    def get_author(self, obj):
        return obj.author.id

    def get_like_count(self, obj):
        return len(obj.likes.all())

    def get_is_liked(self, obj):

        user = self.context.get("user")

        return True if user in obj.likes.all() else False


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = [
            "in_app_notification",
            "banner_notification",
            "vibration",
            "sound",
            "theme",
        ]


class ReportSerializer(serializers.ModelSerializer):
    user = CulturaUserSerializer(source="user_id", read_only=True)
    post = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = "__all__"

    def get_post(self, obj):
        try:
            post_id = ObjectId(obj.post_id)  # Ensure post_id is an ObjectId
            post = Post.objects.get(_id=post_id)
            post_data = PostSerializer(post, context=self.context).data
            author_id = post_data.get("author", {})
            if author_id:
                cultura_user = CulturaUser.objects.get(user_id=author_id)
                post_data["author_data"] = CulturaUserSerializer(
                    cultura_user, context=self.context
                ).data
            return post_data
        except Post.DoesNotExist:
            return None

    def create(self, validated_data):
        validated_data["post_id"] = str(
            validated_data["post_id"]
        )  # Convert ObjectId to string
        return super().create(validated_data)


class ItinerarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Itinerary
        fields = "__all__"


class SaveItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveItinerary
        fields = "__all__"
