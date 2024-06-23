from django.contrib import admin
from .models import CulturaUser, Itinerary, Post, Comment, SaveItinerary


class CulturaUserAdmin(admin.ModelAdmin):
    list_display = (
        # "id",
        "user",
        "fullname",
        "country",
        "email",
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
        "country",
        "date_posted",
        # "image_url",
        "itinerary",
        "likes",
        
    )

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
        'place_image',
        'title',
        'longitude',
        'latitude',
        'place_name',
        'description',
        'budget',
        'status'
    )
class SaveItineraryAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'itineraries',
        'status'
    )

admin.site.register(CulturaUser, CulturaUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(SaveItinerary, SaveItineraryAdmin)

