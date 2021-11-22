from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .models import ExtendedUser
from Encode.models import ImageName
from profileManagement.models import MyProfile
from phonenumbersvalidity import checkNumber
from name_validity import checkName
from django.contrib.auth.decorators import login_required


def registration(request):
    FirstName = LastName = Email = Phone_Number = UserName = ""
    FirstNameError = LastNameError = UserError = PasswordError = PhoneError = ""
    # After Clicking Submit Button
    if request.method == "POST":
        UserName = request.POST['username']
        Pass1 = request.POST['password1']
        Pass2 = request.POST['password2']
        if Pass1 == Pass2:
            try:
                user = User.objects.get(username=UserName)
                UserError = "Username has already been taken!"
            except User.DoesNotExist:
                FirstName = request.POST['firstname']
                LastName = request.POST['lastname']
                Email = request.POST['email']
                Email_Visibility = request.POST['email_visibility']
                Phone_Number = request.POST['phone_number']
                Phone_Number_Visibility = request.POST['phone_number_visibility']
                Gender = request.POST['gender']
                Gender_Visibility = request.POST['gender_visibility']

                if checkNumber(Phone_Number) == 1 and checkName(FirstName) == 1 and checkName(LastName) == 1:
                    user = User.objects.create_user(username=UserName, password=Pass1)
                    initial_image_name = ImageName(name=UserName+"_0", user=user)
                    UsersExtraInfo = ExtendedUser(first_name=FirstName.capitalize(),
                                                  last_name=LastName.capitalize(),
                                                  email=Email.lower(),
                                                  email_visibility=Email_Visibility,
                                                  phone_number=Phone_Number,
                                                  phone_number_visibility=Phone_Number_Visibility,
                                                  gender=Gender,
                                                  gender_visibility=Gender_Visibility,
                                                  user=user)
                    if Gender == "Male":
                        profile_info = MyProfile(nickname=LastName.capitalize(),
                                                 profile_pic='default/male_profile.jpg',
                                                 cover_pic='default/cover.jpg',
                                                 user=user)
                    elif Gender == "Female":
                        profile_info = MyProfile(nickname=LastName.capitalize(),
                                                 profile_pic='default/female_profile.jpg',
                                                 cover_pic='default/cover.jpg',
                                                 user=user)
                    else:
                        profile_info = MyProfile(nickname=LastName.capitalize(),
                                                 profile_pic='default/trans_gender_profile.jpg',
                                                 cover_pic='default/cover.jpg',
                                                 user=user)

                    profile_info.save()
                    UsersExtraInfo.save()
                    initial_image_name.save()
                    return redirect('login')
                elif checkNumber(Phone_Number) == 1 and checkName(FirstName) == 1 and checkName(LastName) == 0:
                    LastNameError = "Invalid Last Name!"
                elif checkNumber(Phone_Number) == 1 and checkName(FirstName) == 0 and checkName(LastName) == 1:
                    FirstNameError = "Invalid First Name!"
                elif checkNumber(Phone_Number) == 1 and checkName(FirstName) == 0 and checkName(LastName) == 0:
                    FirstNameError = "Invalid First Name!"
                    LastNameError = "Invalid Last Name!"
                elif checkNumber(Phone_Number) == 0 and checkName(FirstName) == 1 and checkName(LastName) == 1:
                    PhoneError = "Invalid Phone Number!"
                elif checkNumber(Phone_Number) == 0 and checkName(FirstName) == 1 and checkName(LastName) == 0:
                    PhoneError = "Invalid Phone Number!"
                    LastNameError = "Invalid Last Name!"
                elif checkNumber(Phone_Number) == 0 and checkName(FirstName) == 0 and checkName(LastName) == 1:
                    PhoneError = "Invalid Phone Number!"
                    FirstNameError = "Invalid First Name!"
                elif checkNumber(Phone_Number) == 0 and checkName(FirstName) == 0 and checkName(LastName) == 0:
                    PhoneError = "Invalid Phone Number!"
                    FirstNameError = "Invalid First Name!"
                    LastNameError = "Invalid Last Name!"
        else:
            PasswordError = "Passwords don't match!"

    context = {
        'UserError': UserError,
        'PasswordError': PasswordError,
        'FirstNameError': FirstNameError,
        'LastNameError': LastNameError,
        'PhoneError': PhoneError,

        'FirstName': FirstName,
        'LastName': LastName,
        'Email': Email,
        'Phone_Number': Phone_Number,
        'UserName': UserName
    }
    return render(request, 'registration/registration.html', context)


def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Username or Password')
        else:
            messages.error(request, 'Invalid Username or Password')
    return render(request, 'registration/login_user.html', {'form': form})


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out!')
    return redirect('home')
