str1=list(input())
str2=list(input())
flag=2
for i in range(min(len(str1),len(str2))):
    if str1[i]!=str2[i]:
        flag-=1
if abs(len(str1)-len(str2))>=2:
    print('no')
elif flag>0:
    print('yes')
else:
    print('no')
