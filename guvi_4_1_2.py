
a=input("\nEnter the N number")

b=input("\nEnter the K number")

g=list(str(a))

e=b

while e>0:

    e=e-1

    del(g[e])

print(''.join(g))
