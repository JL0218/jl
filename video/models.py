from django.db import models
from django.contrib.auth.models import User

class VideoCategory(models.Model):
    """视频分类表"""
    name = models.CharField(max_length=50, verbose_name="分类名称")
    slug = models.SlugField(unique=True, verbose_name="URL别名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "视频分类"
        verbose_name_plural = "视频分类"

class Video(models.Model):
    """视频信息表"""
    title = models.CharField(max_length=200, verbose_name="标题")
    cover = models.ImageField(upload_to="covers/", verbose_name="封面图")
    video_file = models.FileField(upload_to="videos/", verbose_name="视频文件")
    description = models.TextField(verbose_name="简介")
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE, verbose_name="分类")
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="上传者")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")
    view_count = models.PositiveIntegerField(default=0, verbose_name="播放量")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = "视频"