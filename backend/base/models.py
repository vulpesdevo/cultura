from djongo import models
from django.db import models as db_models

# from djongo import models as djongo_models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser
from djongo.models.fields import ObjectIdField


# Create your models here.
class CulturaUser(models.Model):
    user = models.CharField(max_length=255)
    fullname = models.CharField(max_length=120)
    country = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)


class Comment(models.Model):
    _id = ObjectIdField()
    user_id = models.CharField(max_length=255,)
    author = models.CharField(max_length=255)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    objects = models.DjongoManager()


class Post(models.Model):
    _id = ObjectIdField()
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comments = models.ArrayField(model_container=Comment, null=True, blank=True)

    objects = models.DjongoManager()
    def add_comment(self, comment):
        self.comments.append(comment)
        self.save()
