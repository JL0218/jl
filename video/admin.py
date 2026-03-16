from django.contrib import admin
from .models import Video, VideoCategory

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploader', 'category', 'created_at', 'view_count')
    search_fields = ('title', 'description')
    list_filter = ('category', 'created_at')

@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')