# 0 means Invalid First or Last Name
# 1 means Valid First or Last Name
def checkName(x):
    BREAK = False
    for i in range(0, len(x)):
        if "A" <= x[i] <= "Z" or "a" <= x[i] <= "z":
            pass
        else:
            BREAK = True
            break
    if BREAK:
        return 0
    else:
        return 1
