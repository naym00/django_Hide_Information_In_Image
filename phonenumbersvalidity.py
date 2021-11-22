# 0 means Invalid Phone Number
# 1 means Valid Phone Number
def checkNumber(x):
    flag = 1
    if len(x) == 14:
        if x[0] == '+' and x[1] == '8' and x[2] == '8' and x[3] == '0' and x[4] == '1':
            for i in range(5, len(x), 1):
                if '0' <= x[i] <= '9':
                    flag = 1
                else:
                    flag = 0
                    break
        else:
            flag = 0

    elif len(x) == 11:
        if x[0] == '0' and x[1] == '1':
            for i in range(2, len(x), 1):
                if '0' <= x[i] <= '9':
                    flag = 1
                else:
                    flag = 0
                    break
        else:
            flag = 0
    else:
        flag = 0
    return flag
