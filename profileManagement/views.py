from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from name_validity import checkName
from phonenumbersvalidity import checkNumber
from registration.models import ExtendedUser
from .forms import NicknamesForm, ProfilePicsForm, CoverPicsForm
from .models import Nicknames, ProfilePics, CoverPics, MyProfile

from pathlib import Path
import cv2


# Create your views here.

@login_required(login_url='/login/')
def profile(request):
    infos = ExtendedUser.objects.get(user=request.user)
    pro_info = MyProfile.objects.get(user=request.user)

    context = {
        'uname': request.user.username,
        'infos': infos,
        'pro_info': pro_info
    }
    return render(request, 'profileManagement/profile.html', context)


@login_required(login_url='/login/')
def update_profile(request):
    infos = ExtendedUser.objects.get(user=request.user)
    FirstNameError = LastNameError = PhoneNumberError = ""

    infos = ExtendedUser.objects.get(user=request.user)
    FirstName = infos.first_name
    LastName = infos.last_name
    Email = infos.email
    Email_Visibility = infos.email_visibility
    Phone_Number = infos.phone_number
    Phone_Number_Visibility = infos.phone_number_visibility
    Gender = infos.gender
    Gender_Visibility = infos.gender_visibility

    if request.method == "POST":

        FirstName = request.POST['firstname'].capitalize()
        LastName = request.POST['lastname'].capitalize()

        Email = request.POST['email'].lower()
        Email_Visibility = request.POST['email_visibility']

        Phone_Number = request.POST['phone_number']
        Phone_Number_Visibility = request.POST['phone_number_visibility']

        Gender = request.POST['gender']
        Gender_Visibility = request.POST['gender_visibility']

        if checkName(FirstName) == 1 and checkName(LastName) == 1 and checkNumber(Phone_Number) == 1:
            infos.first_name = FirstName
            infos.last_name = LastName
            infos.email = Email
            infos.email_visibility = Email_Visibility
            infos.phone_number = Phone_Number
            infos.phone_number_visibility = Phone_Number_Visibility
            infos.gender = Gender
            infos.gender_visibility = Gender_Visibility

            infos.save(update_fields=['first_name',
                                      'last_name',
                                      'email',
                                      'email_visibility',
                                      'phone_number',
                                      'phone_number_visibility',
                                      'gender',
                                      'gender_visibility'])
            return redirect('profile')

        elif checkName(FirstName) == 1 and checkName(LastName) == 1 and checkNumber(
                Phone_Number) == 0:
            PhoneNumberError = "Invalid Phone Number!"
        elif checkName(FirstName) == 1 and checkName(LastName) == 0 and checkNumber(
                Phone_Number) == 1:
            LastNameError = "Invalid Last Name"
        elif checkName(FirstName) == 1 and checkName(LastName) == 0 and checkNumber(
                Phone_Number) == 0:
            LastNameError = "Invalid Last Name"
            PhoneNumberError = "Invalid Phone Number!"
        elif checkName(FirstName) == 0 and checkName(LastName) == 1 and checkNumber(
                Phone_Number) == 1:
            FirstNameError = "Invalid First Name"
        elif checkName(FirstName) == 0 and checkName(LastName) == 1 and checkNumber(
                Phone_Number) == 0:
            FirstNameError = "Invalid First Name"
            PhoneNumberError = "Invalid Phone Number!"
        elif checkName(FirstName) == 0 and checkName(LastName) == 0 and checkNumber(
                Phone_Number) == 1:
            FirstNameError = "Invalid First Name"
            LastNameError = "Invalid Last Name"
        elif checkName(FirstName) == 0 and checkName(LastName) == 0 and checkNumber(
                Phone_Number) == 0:
            FirstNameError = "Invalid First Name"
            LastNameError = "Invalid Last Name"
            PhoneNumberError = "Invalid Phone Number!"

    context = {
        'infos': infos,
        'FirstName': FirstName,
        'LastName': LastName,
        'Email': Email,
        'Phone_Number': Phone_Number,

        'FirstNameError': FirstNameError,
        'LastNameError': LastNameError,
        'PhoneNumberError': PhoneNumberError
    }
    if (Email_Visibility == "True") and (Phone_Number_Visibility == "True") and (Gender_Visibility == "True"):
        if Gender == "Male":
            return render(request, 'profileManagement/update_profile/update_profile1.html', context)
        elif Gender == "Female":
            return render(request, 'profileManagement/update_profile/update_profile2.html', context)
        else:
            return render(request, 'profileManagement/update_profile/update_profile3.html', context)
    elif (Email_Visibility == "True") and (Phone_Number_Visibility == "True") and (Gender_Visibility == "False"):
        if Gender == "Male":
            return render(request, 'profileManagement/update_profile/update_profile4.html', context)
        elif Gender == "Female":
            return render(request, 'profileManagement/update_profile/update_profile5.html', context)
        else:
            return render(request, 'profileManagement/update_profile/update_profile6.html', context)
    elif (Email_Visibility == "True") and (Phone_Number_Visibility == "False") and (Gender_Visibility == "True"):
        if Gender == "Male":
            return render(request, 'profileManagement/update_profile/update_profile7.html', context)
        elif Gender == "Female":
            return render(request, 'profileManagement/update_profile/update_profile8.html', context)
        else:
            return render(request, 'profileManagement/update_profile/update_profile9.html', context)
    elif (Email_Visibility == "True") and (Phone_Number_Visibility == "False") and (Gender_Visibility == "False"):
        if Gender == "Male":
            return render(request, 'profileManagement/update_profile/update_profile10.html', context)
        elif Gender == "Female":
            return render(request, 'profileManagement/update_profile/update_profile11.html', context)
        else:
            return render(request, 'profileManagement/update_profile/update_profile12.html', context)
    elif (Email_Visibility == "False") and (Phone_Number_Visibility == "True") and (Gender_Visibility == "True"):
        if Gender == "Male":
            return render(request, 'profileManagement/update_profile/update_profile13.html', context)
        elif Gender == "Female":
            return render(request, 'profileManagement/update_profile/update_profile14.html', context)
        else:
            return render(request, 'profileManagement/update_profile/update_profile15.html', context)
    elif (Email_Visibility == "False") and (Phone_Number_Visibility == "True") and (Gender_Visibility == "False"):
        if Gender == "Male":
            return render(request, 'profileManagement/update_profile/update_profile16.html', context)
        elif Gender == "Female":
            return render(request, 'profileManagement/update_profile/update_profile17.html', context)
        else:
            return render(request, 'profileManagement/update_profile/update_profile18.html', context)
    elif (Email_Visibility == "False") and (Phone_Number_Visibility == "False") and (Gender_Visibility == "True"):
        if Gender == "Male":
            return render(request, 'profileManagement/update_profile/update_profile19.html', context)
        elif Gender == "Female":
            return render(request, 'profileManagement/update_profile/update_profile20.html', context)
        else:
            return render(request, 'profileManagement/update_profile/update_profile21.html', context)
    elif (Email_Visibility == "False") and (Phone_Number_Visibility == "False") and (Gender_Visibility == "False"):
        if Gender == "Male":
            return render(request, 'profileManagement/update_profile/update_profile22.html', context)
        elif Gender == "Female":
            return render(request, 'profileManagement/update_profile/update_profile23.html', context)
        else:
            return render(request, 'profileManagement/update_profile/update_profile24.html', context)


@login_required(login_url='/login/')
def insert_nickname(request):
    infos = ExtendedUser.objects.get(user=request.user)
    form = NicknamesForm()
    if request.method == "POST":
        form = NicknamesForm(request.POST)
        if form.is_valid:
            new_nickname = Nicknames(nickname=request.POST['nickname'],
                                     user=request.user)
            new_nickname.save()
            return redirect('profile')
    return render(request, 'profileManagement/insert_nickname.html', {'form': form, 'infos': infos})


@login_required(login_url='/login/')
def insert_profile_pic(request):
    infos = ExtendedUser.objects.get(user=request.user)
    form = ProfilePicsForm()
    if request.method == "POST":
        form = ProfilePicsForm(request.FILES)
        if form.is_valid:
            new_profile_pic = ProfilePics(profile_pic=request.FILES['profile_pic'],
                                          user=request.user)
            new_profile_pic.save()
            return redirect('profile')
    return render(request, 'profileManagement/insert_profile_pic.html', {'form': form, 'infos': infos})


@login_required(login_url='/login/')
def insert_cover_pic(request):
    infos = ExtendedUser.objects.get(user=request.user)
    form = CoverPicsForm()
    if request.method == "POST":
        form = CoverPicsForm(request.FILES)
        if form.is_valid:
            new_cover_photo = CoverPics(cover_pic=request.FILES['cover_pic'],
                                        user=request.user)
            new_cover_photo.save()
            return redirect('profile')
    return render(request, 'profileManagement/insert_cover_pic.html', {'form': form, 'infos': infos})


@login_required(login_url='/login/')
def show_nicknames(request):
    infos = ExtendedUser.objects.get(user=request.user)
    nicknames = Nicknames.objects.filter(user=request.user)
    return render(request, 'profileManagement/show_nicknames.html', {'nicknames': nicknames, 'infos': infos})


@login_required(login_url='/login/')
def show_profile_pics(request):
    infos = ExtendedUser.objects.get(user=request.user)
    profile_pics = ProfilePics.objects.filter(user=request.user)
    return render(request, 'profileManagement/show_profile_pics.html', {'profile_pics': profile_pics, 'infos': infos})


@login_required(login_url='/login/')
def show_cover_pics(request):
    infos = ExtendedUser.objects.get(user=request.user)
    cover_pics = CoverPics.objects.filter(user=request.user)
    return render(request, 'profileManagement/show_cover_pics.html', {'cover_pics': cover_pics, 'infos': infos})


@login_required(login_url='/login/')
def set_nickname(request, nickname_id):
    nick_name = Nicknames.objects.get(pk=nickname_id)

    info = MyProfile.objects.get(user=request.user)
    info.nickname = nick_name.nickname
    info.save(update_fields=['nickname'])
    return redirect('profile')


@login_required(login_url='/login/')
def set_profile_pic(request, profile_pic_id):
    pro_pic = ProfilePics.objects.get(pk=profile_pic_id)
    info = MyProfile.objects.get(user=request.user)

    info.profile_pic = pro_pic.profile_pic
    info.save(update_fields=['profile_pic'])
    return redirect('profile')


@login_required(login_url='/login/')
def set_cover_pic(request, cover_pic_id):
    cvr_pic = CoverPics.objects.get(pk=cover_pic_id)

    info = MyProfile.objects.get(user=request.user)
    info.cover_pic = cvr_pic.cover_pic
    info.save(update_fields=['cover_pic'])
    return redirect('profile')
