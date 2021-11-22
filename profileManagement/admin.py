from django.contrib import admin
from .models import Nicknames, ProfilePics, CoverPics, MyProfile
# Register your models here.
admin.site.register([Nicknames, ProfilePics, CoverPics, MyProfile])