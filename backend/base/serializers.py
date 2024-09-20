from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
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
    Report
)
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

    ##
    def check_user(self, clean_data):
        user = authenticate(
            username=clean_data["username"], password=clean_data["password"]
        )
        print(user)
        if not user:
            raise ValidationError("user not found")
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "username", "email")


class CulturaUserSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only=True)
    follow_count = serializers.SerializerMethodField()
    is_followed = serializers.SerializerMethodField()

    class Meta:
        model = CulturaUser
        fields = [
            "user",
            "user_photo",
            "fullname",
            "country",
            "email",
            "followers",
            "is_followed",
            "follow_count",
            "is_active",
            "trend_setter",
            "share_star",
            "like_leader",
            "knowledge_seeker",
            "guide_guru",
            "explorer_extraordinaire",
            "cultura_contributor",
            "content_creator",
            "comment_connoisseur",
        ]

    def get_follow_count(self, obj):
        return len(obj.followers.all())

    def get_is_followed(self, obj):
        user = self.context.get("user")
        print("USER : ", user)
        return True if user in obj.followers.all() else False


class CommentSerializer(serializers.ModelSerializer):

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
    class Meta:
        model = Report
        fields = '__all__'
class ItinerarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Itinerary
        fields = "__all__"


class SaveItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveItinerary
        fields = "__all__"
