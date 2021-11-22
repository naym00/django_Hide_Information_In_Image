from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ImageInfo
from registration.models import ExtendedUser
from integer_validity import check_integer
from .encode import encode
from .models import ImageName
from pathlib import Path


# Create your views here.
@login_required(login_url='/login/')
def encode_form(request):
    Title = Hint = ""
    Starting_Index = Gap = Add_a_Value = HiddenData = ""

    Starting_Index_Error = Gap_Error = Add_a_Value_Error = ""
    infos = ExtendedUser.objects.get(user=request.user)
    if request.method == "POST":
        Title = request.POST['Title']
        Starting_Index = request.POST['Starting_Index']
        Gap = request.POST['Gap']
        Add_a_Value = request.POST['Add_a_Value']
        Hint = request.POST['Hint']
        HiddenData = request.POST['HiddenData']

        if check_integer(Starting_Index) == 1 and check_integer(Gap) == 1 and check_integer(Add_a_Value) == 1:
            name_info = ImageName.objects.get(user=request.user)
            Image_Name = name_info.name
            uname, num = Image_Name.split("_")
            name_info.name = uname + "_" + str(int(num) + 1)
            name_info.save(update_fields=['name'])

            SavingPath = str(
                Path(__file__).resolve().parent.parent) + '\media\data_image\\' + Image_Name + '.jpg'
            encode(SavingPath, int(Starting_Index), int(Gap)+1, int(Add_a_Value), HiddenData)
            image_info = ImageInfo(title=Title, data_size=str(len(HiddenData)),
                                   hint=Hint,
                                   data_image='data_image\\' + Image_Name + '.jpg',
                                   user=request.user)
            image_info.save()

            return redirect('profile')

        elif check_integer(Starting_Index) == 1 and check_integer(Gap) == 1 and check_integer(Add_a_Value) == 0:
            Add_a_Value_Error = "Should be an integer number!"
        elif check_integer(Starting_Index) == 1 and check_integer(Gap) == 0 and check_integer(Add_a_Value) == 1:
            Gap_Error = "Should be an integer number!"
        elif check_integer(Starting_Index) == 1 and check_integer(Gap) == 0 and check_integer(Add_a_Value) == 0:
            Gap_Error = "Should be an integer number!"
            Add_a_Value_Error = "Should be an integer number!"
        elif check_integer(Starting_Index) == 0 and check_integer(Gap) == 1 and check_integer(Add_a_Value) == 1:
            Starting_Index_Error = "Should be an integer number!"
        elif check_integer(Starting_Index) == 0 and check_integer(Gap) == 1 and check_integer(Add_a_Value) == 0:
            Starting_Index_Error = "Should be an integer number!"
            Add_a_Value_Error = "Should be an integer number!"
        elif check_integer(Starting_Index) == 0 and check_integer(Gap) == 0 and check_integer(Add_a_Value) == 1:
            Starting_Index_Error = "Should be an integer number!"
            Gap_Error = "Should be an integer number!"
        elif check_integer(Starting_Index) == 0 and check_integer(Gap) == 0 and check_integer(Add_a_Value) == 0:
            Starting_Index_Error = "Should be an integer number!"
            Gap_Error = "Should be an integer number!"
            Add_a_Value_Error = "Should be an integer number!"
    context = {
        'infos': infos,
        'Title': Title,
        'Hint': Hint,

        'Starting_Index': Starting_Index,
        'Gap': Gap,
        'Add_a_Value': Add_a_Value,
        'HiddenData': HiddenData,

        'Starting_Index_Error': Starting_Index_Error,
        'Gap_Error': Gap_Error,
        'Add_a_Value_Error': Add_a_Value_Error
    }
    return render(request, 'Encode/encode_form.html', context)


def encoded_image_list(request):
    info = ImageInfo.objects.filter(user=request.user)
    infos = ExtendedUser.objects.get(user=request.user)
    return render(request, 'Encode/encoded_image_list.html', {'info': info, 'infos': infos})
