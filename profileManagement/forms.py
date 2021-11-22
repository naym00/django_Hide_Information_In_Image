from django import forms
from .models import Nicknames, ProfilePics, CoverPics


class NicknamesForm(forms.ModelForm):
    class Meta:
        model = Nicknames
        fields = ('nickname',)


class ProfilePicsForm(forms.ModelForm):
    class Meta:
        model = ProfilePics
        fields = ('profile_pic',)


class CoverPicsForm(forms.ModelForm):
    class Meta:
        model = CoverPics
        fields = ('cover_pic',)
