n = input()
sum_,odd_ = 0,0
for i in n:
    if(int(i)%2==0):
        sum_ = sum_ + int(i)
    else:
        odd_ = odd_ + int(i)
    
print(sum_,odd_)