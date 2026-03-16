from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """用户扩展信息表"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default.png", verbose_name="头像")
    bio = models.CharField(max_length=200, blank=True, verbose_name="个人简介")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"