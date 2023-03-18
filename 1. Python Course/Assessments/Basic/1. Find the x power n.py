def xRaisedPower(x,n):
    if(x>100):
        return 0
    if(n>10):
        return 0
    if(n<=10 and x<=100):
        return x**n
x = int(input())
n = int(input())
print(xRaisedPower(x,n))