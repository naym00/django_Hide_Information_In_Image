from django.db import models
from django.contrib.auth.models import User


class Nicknames(models.Model):
    nickname = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username


class ProfilePics(models.Model):
    profile_pic = models.ImageField(upload_to='images/profile_pic/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username


class CoverPics(models.Model):
    cover_pic = models.ImageField(upload_to='images/cover_pic/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username


class MyProfile(models.Model):
    nickname = models.CharField(max_length=20)
    profile_pic = models.ImageField()
    cover_pic = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
