from djongo import models
from django.db import models as db_models
from django.utils.translation import gettext as _

# from djongo import models as djongo_models
from django.contrib.auth import get_user_model

from djongo.models.fields import ObjectIdField

# from django.contrib.auth.models import User
from django.contrib.auth.models import User

## models.py
from djongo.storage import GridFSStorage
from django.conf import settings
from profanity.validators import validate_is_profane

# Define your GridFSStorage instance
# grid_fs_storage = GridFSStorage(collection='uploads', base_url=''.join([str(settings.BASE_URL), '/uploads/'])),storage=grid_fs_storage


# Create your models here.
class CulturaUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_photo = models.ImageField(
        blank=True,
        null=True,
        upload_to="profile_pictures",
        default="profile_pictures/default_profile.png",
    )
    fullname = models.CharField(max_length=120)
    country = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    trend_setter = models.IntegerField(default=0, null=True, blank=True)
    share_star = models.IntegerField(default=0, null=True, blank=True)
    like_leader = models.IntegerField(default=0, null=True, blank=True)
    knowledge_seeker = models.IntegerField(default=0, null=True, blank=True)
    guide_guru = models.IntegerField(default=0, null=True, blank=True)
    explorer_extraordinaire = models.IntegerField(default=0, null=True, blank=True)
    cultura_contributor = models.IntegerField(default=0, null=True, blank=True)
    content_creator = models.IntegerField(default=0, null=True, blank=True)
    comment_connoisseur = models.IntegerField(default=0, null=True, blank=True)


class SaveItinerary(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    creator_name = models.CharField(max_length=50)
    main_image = models.ImageField(blank=True, null=True, upload_to="main_images")
    main_title = models.CharField(max_length=255, validators=[validate_is_profane])
    main_description = models.CharField(
        max_length=255, validators=[validate_is_profane]
    )
    gen_tips = models.CharField(max_length=255, validators=[validate_is_profane])
    currency = models.CharField(
        max_length=255,
    )
    total_budget = models.FloatField()
    itineraries = models.CharField(default=list, max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


class Itinerary(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    creator_name = models.CharField(max_length=50)
    place_image = models.ImageField(upload_to="place_images", null=True, blank=True)
    title = models.CharField(max_length=255, validators=[validate_is_profane])
    longitude = models.FloatField()
    latitude = models.FloatField()
    place_name = models.CharField(max_length=255)
    description = models.TextField(validators=[validate_is_profane])
    code = models.CharField(blank=True, null=True, max_length=50)
    budget = models.FloatField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="onqueue", max_length=255)


class Comment(models.Model):
    _id = ObjectIdField()
    post_id = models.CharField(max_length=255, null=True)
    replied_to = models.CharField(
        max_length=255,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(validators=[validate_is_profane])
    date_posted = models.DateTimeField(auto_now_add=True)


from django.utils import timezone


class Post(models.Model):
    _id = ObjectIdField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=200, validators=[validate_is_profane])
    category = models.CharField(max_length=255, default=None)
    content = models.TextField(validators=[validate_is_profane])
    image = models.ImageField(upload_to="post_images", null=True, blank=True)
    country = models.CharField(max_length=200)
    itinerary = models.CharField( 
        max_length=200, null=True, blank=True
    )
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)


class LikeNotification(models.Model):
    _id = ObjectIdField()
    post_author = models.CharField(max_length=255)
    post_obj_id = models.CharField(max_length=255)
    post_title = models.CharField(max_length=255, validators=[validate_is_profane])
    post_content = models.CharField(max_length=255, validators=[validate_is_profane])
    notif_type = models.CharField(max_length=255)
    audience = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


class UserSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="settings")
    in_app_notification = models.BooleanField(default=False)
    banner_notification = models.BooleanField(default=False)
    vibration = models.BooleanField(default=False)
    sound = models.BooleanField(default=False)
    theme = models.BooleanField(default=False)


