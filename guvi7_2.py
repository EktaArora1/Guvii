zeroOfones=0
s=input()
for i in s:
    if i=='0' or i=='1':
        zeroOfones+=1
print('yes') if len(s)==zeroOfones else print('no')
