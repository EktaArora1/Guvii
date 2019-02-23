alphacount=0
numcount=0
s=input()
for i in s:
    if i>='0' and i<='9':
        numcount+=1
    if i>='a' and i<='z':
        alphacount+=1
    if i>='A' and i<='Z':
        alphacount+=1
print('yes') if numcount>0 and alphacount>0 else print('no')
