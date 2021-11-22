from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from registration.models import ExtendedUser


# Create your views here.
def home(request):
    infos = ""
    if request.user.is_authenticated:
        infos = ExtendedUser.objects.get(user=request.user)
    return render(request, 'HomeManagement/Home.html', {'infos': infos})


@login_required(login_url='/login/')
def user_list(request):
    users = ExtendedUser.objects.all()
    infos = ExtendedUser.objects.get(user=request.user)

    for i in range(0, len(users)):
        if (users[i].email_visibility == "True") and (users[i].phone_number_visibility == "True") and (
                users[i].gender_visibility == "True"):
            users[i].email_carrier = users[i].email
            users[i].phone_number_carrier = users[i].phone_number
            users[i].gender_carrier = users[i].gender

        elif (users[i].email_visibility == "True") and (users[i].phone_number_visibility == "True") and (
                users[i].gender_visibility == "False"):
            users[i].email_carrier = users[i].email
            users[i].phone_number_carrier = users[i].phone_number
            users[i].gender_carrier = "Private"

        elif (users[i].email_visibility == "True") and (users[i].phone_number_visibility == "False") and (
                users[i].gender_visibility == "True"):
            users[i].email_carrier = users[i].email
            users[i].phone_number_carrier = "Private"
            users[i].gender_carrier = users[i].gender

        elif (users[i].email_visibility == "True") and (users[i].phone_number_visibility == "False") and (
                users[i].gender_visibility == "False"):
            users[i].email_carrier = users[i].email
            users[i].phone_number_carrier = "Private"
            users[i].gender_carrier = "Private"

        elif (users[i].email_visibility == "False") and (users[i].phone_number_visibility == "True") and (
                users[i].gender_visibility == "True"):
            users[i].email_carrier = "Private"
            users[i].phone_number_carrier = users[i].phone_number
            users[i].gender_carrier = users[i].gender

        elif (users[i].email_visibility == "False") and (users[i].phone_number_visibility == "True") and (
                users[i].gender_visibility == "False"):
            users[i].email_carrier = "Private"
            users[i].phone_number_carrier = users[i].phone_number
            users[i].gender_carrier = "Private"

        elif (users[i].email_visibility == "False") and (users[i].phone_number_visibility == "False") and (
                users[i].gender_visibility == "True"):
            users[i].email_carrier = "Private"
            users[i].phone_number_carrier = "Private"
            users[i].gender_carrier = users[i].gender

        elif (users[i].email_visibility == "False") and (users[i].phone_number_visibility == "False") and (
                users[i].gender_visibility == "False"):
            users[i].email_carrier = "Private"
            users[i].phone_number_carrier = "Private"
            users[i].gender_carrier = "Private"

    return render(request, 'HomeManagement/user_list.html', {'users': users, 'infos': infos})
