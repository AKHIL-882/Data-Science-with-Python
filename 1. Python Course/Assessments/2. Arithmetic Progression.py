def arithmeticProgression(x1,x2,x3):
    if(x1>100 or x2>100 or x3>100):
        return 0;
    else:
        checkDiff1 = abs(x2-x1)
        checkDiff2 = abs(x3-x2)
        if(checkDiff1==checkDiff2):
            return checkDiff2
        else:
            return 0;
x1 = int(input())
x2 = int(input())
x3 = int(input())
print(arithmeticProgression(x1,x2,x3))
        