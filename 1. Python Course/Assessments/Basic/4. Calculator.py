def takeInputsMod():
    num1 = int(input())
    num2 = int(input())
    return num1%num2
def takeInputsDiv():
    num1 = int(input())
    num2 = int(input())
    return num1/num2
def takeInputsMul():
    num1 = int(input())
    num2 = int(input())
    return num1*num2
def takeInputsSub():
    num1 = int(input())
    num2 = int(input())
    return num1-num2
def takeInputsAdd():
    num1 = int(input())
    num2 = int(input())
    return num1+num2
    
n = int(input())
if(n==6):
    pass
elif(n==5):
    print(takeInputsMod())
elif(n==4):
    print(takeInputsDiv())
elif(n==3):
    print(takeInputsMul())
elif(n==2):
    print(takeInputsSub())
else:
    print(takeInputsAdd())
    
    
    
