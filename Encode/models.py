from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ImageInfo(models.Model):
    title = models.CharField(max_length=200)
    data_size = models.CharField(max_length=100)
    hint = models.CharField(max_length=200)
    data_image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username


class ImageName(models.Model):
    name = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
