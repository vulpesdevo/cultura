from djongo import models
from django.db import models as db_models
from django.utils.translation import gettext as _
# from djongo import models as djongo_models
from django.contrib.auth import get_user_model

from djongo.models.fields import ObjectIdField
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group

## models.py
from djongo.storage import GridFSStorage
from django.conf import settings

# Define your GridFSStorage instance
# grid_fs_storage = GridFSStorage(collection='uploads', base_url=''.join([str(settings.BASE_URL), '/uploads/'])),storage=grid_fs_storage

# Create your models here.
class CulturaUser(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    fullname = models.CharField(max_length=120)
    country = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

class SaveItinerary(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    creator_name = models.CharField(max_length=50)
    main_image = models.ImageField(blank=True, null=True,upload_to='main_images' )
    main_title = models.CharField(max_length=255)
    main_description = models.CharField(max_length=255)
    gen_tips = models.CharField(max_length=255,)
    total_budget = models.FloatField()
    itineraries= models.CharField(default=list, max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
class Itinerary(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    creator_name = models.CharField(max_length=50)
    place_image = models.ImageField(upload_to='place_images',null=True,blank=True)
    title = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    place_name = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.FloatField(null=True,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
class Comment(models.Model):
    _id = ObjectIdField()
    post_id = models.CharField(
        max_length=255, null=True
    )
    replied_to = models.CharField(
        max_length=255,
    )
    author = models.CharField(max_length=255)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    


class Post(models.Model):
    _id = ObjectIdField()
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=255,default=None)
    content = models.TextField()
    image= models.ImageField(upload_to="post_images",null=True,blank=True)
    country = models.CharField(max_length=200)
    itinerary = models.CharField(max_length=200,null=True,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    


# class AppUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("An email is required.")
#         if not password:
#             raise ValueError("A password is required.")
#         if not username:
#             raise ValueError("A username is required.")
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, username, password=None):
#         if not email:
#             raise ValueError("An email is required.")
#         if not password:
#             raise ValueError("A password is required.")
#         if not username:
#             raise ValueError("A username is required.")
#         user = self.create_user(email, username, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user


# class AppUser(AbstractBaseUser, PermissionsMixin):
#     user_id = models.AutoField(primary_key=True)
#     email = models.EmailField(max_length=50)
#     username = models.CharField(max_length=50, unique=True)
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]
#     objects = AppUserManager()
#     groups = models.ManyToManyField(Group)
#     def __str__(self):
#         return self.username
