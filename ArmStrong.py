a=input()
b=len(a)
c=list()
a=int(a)
t=a
for i in range(b):
    r=t%10
    t=t//10
    c.append(r)
s=0
for k in c:
    s += k**b
if(s==a):
    print('yes')
else:
    print('no')
