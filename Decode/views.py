from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Encode.models import ImageInfo
from registration.models import ExtendedUser
from integer_validity import check_integer
from .decode import decode
from pathlib import Path


def original(x):
    if 1 <= x <= 10:
        return 0
    elif 11 <= x <= 20:
        return 1
    elif 21 <= x <= 30:
        return 2
    elif 31 <= x <= 40:
        return 3
    elif 41 <= x <= 50:
        return 4
    elif 51 <= x <= 60:
        return 5
    elif 61 <= x <= 70:
        return 6
    elif 71 <= x <= 80:
        return 7
    elif 81 <= x <= 90:
        return 8
    elif 91 <= x <= 100:
        return 9
    else:
        return 0


# Create your views here.

@login_required(login_url='/login/')
def decode_form(request, image_id):
    Image_Id = image_id
    Starting_Index = ""
    Gap = ""
    Add_a_Value = ""

    Starting_Index_Error = ""
    Gap_Error = ""
    Add_a_Value_Error = ""
    infos = ExtendedUser.objects.get(user=request.user)
    if request.method == "POST":
        Starting_Index = request.POST['Starting_Index']
        Gap = request.POST['Gap']
        Add_a_Value = request.POST['Add_a_Value']

        if check_integer(Starting_Index) == 1 and check_integer(Gap) == 1 and check_integer(Add_a_Value) == 1:
            image_info = ImageInfo.objects.get(pk=image_id)
            ImagePath = str(Path(__file__).resolve().parent.parent) + image_info.data_image.url.replace("/", "\\", 3)

            data = decode(int(Starting_Index), int(Gap)+1, int(Add_a_Value), int(image_info.data_size), ImagePath)
            return render(request, 'Decode/decoded_data.html', {'data': data, 'infos': infos})
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
        'Image_Id': Image_Id,
        'Starting_Index': Starting_Index,
        'Gap': Gap,
        'Add_a_Value': Add_a_Value,

        'Starting_Index_Error': Starting_Index_Error,
        'Gap_Error': Gap_Error,
        'Add_a_Value_Error': Add_a_Value_Error
    }
    return render(request, 'Decode/decode_form.html', context)


def deleteRow(request, row_id):
    data = ImageInfo.objects.get(pk=row_id)
    data.delete()
    return redirect('encoded_image_list')
