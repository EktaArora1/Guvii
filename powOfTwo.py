import math
n=int(input())
flag=0
def po(n):
    if n==1:
        flag=0
        return flag
    if n==2:
        flag=1
        return flag
    return po(math.floor(n/2))
c=po(n)
print("yes" if c==1 else "no")
