import cv2


def original(x):
    if 1 <= x <= 20:
        return 0
    elif 21 <= x <= 40:
        return 1
    elif 41 <= x <= 60:
        return 2
    elif 61 <= x <= 80:
        return 3
    elif 81 <= x <= 100:
        return 4
    elif 101 <= x <= 120:
        return 5
    elif 121 <= x <= 140:
        return 6
    elif 141 <= x <= 160:
        return 7
    elif 161 <= x <= 180:
        return 8
    elif 181 <= x <= 200:
        return 9
    else:
        return 0


def decode(Starting_Index, Gap, Add_a_Value, LengthOfString, ImagePath):
    image = cv2.imread(ImagePath)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    Row, Column = gray_image.shape
    whichTimes = gapCounter = 1
    k = Start = inserting3 = Value = Counter = 0
    DecodedString = ""

    for i in range(0, Row, 1):
        for j in range(0, Column, 1):

            if Counter == Starting_Index:
                Start = 1
                inserting3 = 1
            if Start == 1:
                if k == LengthOfString:
                    k = -1
                    break
                else:
                    if inserting3 == 0:
                        if gapCounter == Gap:
                            inserting3 = 1
                            whichTimes = 1
                            gapCounter = 1
                        else:
                            gapCounter = gapCounter + 1

                    elif inserting3 == 1:
                        if whichTimes == 1:
                            Value = 0
                            Value = Value + original(gray_image[i, j]) * 100
                            whichTimes = 2
                        elif whichTimes == 2:
                            Value = Value + original(gray_image[i, j]) * 10
                            whichTimes = 3
                        else:
                            Value = Value + original(gray_image[i, j])

                            while Value < Add_a_Value:
                                Value = Value + 255
                            DecodedString = DecodedString + chr(Value - Add_a_Value)
                            k = k + 1
                            inserting3 = 0
            Counter = Counter + 1
        if k == -1:
            break
    return DecodedString
