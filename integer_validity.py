def check_integer(x):
    Okay = True
    for i in range(0, len(x)):
        if '0' <= x[i] <= '9':
            pass
        else:
            Okay = False
            break
    if Okay:
        return 1
    else:
        return 0
