arr=input()
n=['1','2','3','4','5','6','7','8','9','0']
c=0
for i in arr:
    if i in n:
        c+=1
print(c)
