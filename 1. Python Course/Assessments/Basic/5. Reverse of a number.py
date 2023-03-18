n = input()
n_rev = n[::-1]
if(n_rev[0]=="0"):
    print(n_rev[1:])
else:
    print(n_rev)