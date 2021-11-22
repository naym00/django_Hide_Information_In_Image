import math
import random
import cv2
import numpy as np

listForRandomInsert = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]


def duplicate(x):
    if x == 0:
        return 10
    elif x == 1:
        return 30
    elif x == 2:
        return 50
    elif x == 3:
        return 70
    elif x == 4:
        return 90
    elif x == 5:
        return 110
    elif x == 6:
        return 130
    elif x == 7:
        return 150
    elif x == 8:
        return 170
    elif x == 9:
        return 190


def encode(SavingPath, Starting_Index, Gap, Add_a_Value, HiddenData):
    LengthOfString = len(HiddenData)
    rowCol = int(math.sqrt(Starting_Index + 3 * LengthOfString + (LengthOfString - 1) * Gap)) + 1
    image = np.zeros((rowCol, rowCol, 3), np.uint8)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    whichTimes = gapCounter = 1
    k = Start = inserting3 = dataWillBeStore = Counter = 0
    for i in range(0, rowCol, 1):
        for j in range(0, rowCol, 1):
            gray_image[i, j] = listForRandomInsert[random.randint(0, 9)]

            if Counter == Starting_Index:
                Start = 1
                inserting3 = 1
            if Start == 1:
                if k == LengthOfString:
                    Start = 0
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
                            dataWillBeStore = ord(HiddenData[k]) + Add_a_Value
                            while dataWillBeStore > 255:
                                dataWillBeStore = dataWillBeStore - 255
                            gray_image[i, j] = duplicate(int(dataWillBeStore / 100))
                            whichTimes = 2
                        elif whichTimes == 2:
                            gray_image[i, j] = duplicate(int(dataWillBeStore / 10) % 10)
                            whichTimes = 3
                        else:
                            gray_image[i, j] = duplicate(dataWillBeStore % 10)
                            k = k + 1
                            inserting3 = 0
            Counter = Counter + 1
    cv2.imwrite(SavingPath, gray_image)
