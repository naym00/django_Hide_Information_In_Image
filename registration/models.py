from django.db import models
from django.contrib.auth.models import User


class ExtendedUser(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    email = models.EmailField(unique=True)
    email_visibility = models.CharField(max_length=10)
    email_carrier = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=20, unique=True)
    phone_number_visibility = models.CharField(max_length=10)
    phone_number_carrier = models.CharField(max_length=20)

    gender = models.CharField(max_length=20)
    gender_visibility = models.CharField(max_length=10)
    gender_carrier = models.CharField(max_length=20)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
