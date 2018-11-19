a=input()
b=len(a)
c=list()
a=int(a)
t=a
for i in range(b):
    r=t%10
    t=t//10
    c.append(r)
print(c)

s=0
for k in c:
    s += k**b
print(s)
print(a)
if(s==a):
    print('yes')
else:
    print('no')
