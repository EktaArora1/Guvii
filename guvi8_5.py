str1=list(input())
l=len(str1)
if l%2==1:
    str1[l//2]='*'
else:
    str1[l//2]='*'
    str1[l//2+1]='*'
print("".join(str1))
