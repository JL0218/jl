from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("video/<int:pk>/", views.video_detail, name="video_detail"),
    path("category/<slug:slug>/", views.category_videos, name="category_videos"),
    path("upload/", views.upload_video, name="upload_video"),
]