from django.contrib import admin
from .models import CulturaUser, Itinerary, LikeNotification, Post, Comment, SaveItinerary, UserSetting


class CulturaUserAdmin(admin.ModelAdmin):
    list_display = (
        # "id",
        "user",
        "user_photo",
        "fullname",
        "country",
        "email",
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
    )

    def cultura_user_info(self, obj):
        return obj.description  # replace with the actual field you want to display


class PostAdmin(admin.ModelAdmin):
    list_display = ('_id', 'author', 'title','content', 'category','image', 'country', 'date_posted')

    def post_info(self, obj):
        return obj.description  # replace with the actual field you want to display


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        # "_id",
        "post_id",
        "author",
        "replied_to",
        "body",
        "date_posted",
    )

    def comment_info(self, obj):
        return obj.description  # replace with the actual field you want to display
class ItineraryAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'creator_name',
        'place_image',
        'title',
        'longitude',
        'latitude',
        'place_name',
        'description',
        'code',
        'budget',
        'status'
    )
class SaveItineraryAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'creator_name',
        'main_image',
        'main_title',
        'main_description',
        'gen_tips',
        'currency',
        'total_budget',
        'itineraries',
        'status'
    )
class LikeNotificationAdmin(admin.ModelAdmin):
    list_display = (

        'post_obj_id',
        'notif_type',
        'post_author',
        'post_title',
        'post_content',
        'audience',
        'is_read',
        'created_at',
    )


class UserSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'in_app_notification',
        'banner_notification',
        'vibration',
        'sound',
        'theme',
    )




admin.site.register(UserSetting, UserSettingsAdmin)

admin.site.register(LikeNotification, LikeNotificationAdmin)
admin.site.register(CulturaUser, CulturaUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(SaveItinerary, SaveItineraryAdmin)

