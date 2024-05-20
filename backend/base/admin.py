from django.contrib import admin
from .models import CulturaUser, Post, Comment


class CulturaUserAdmin(admin.ModelAdmin):
    list_display = (
        # "_id",
        "user",
        "first_name",
        "last_name",
        "location",
        "email",
        "contact",
        "is_active",
    )

    def cultura_user_info(self, obj):
        return obj.description  # replace with the actual field you want to display


class PostAdmin(admin.ModelAdmin):
    list_display = (
        # "_id",
        "title",
        "author",
        "content",
        "date_posted",
        # "image_url",
        "likes",
        "comments",
    )

    def post_info(self, obj):
        return obj.description  # replace with the actual field you want to display


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        # "_id",
        "author",
        "body",
        "date_posted",
    )

    def comment_info(self, obj):
        return obj.description  # replace with the actual field you want to display


admin.site.register(CulturaUser, CulturaUserAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)
