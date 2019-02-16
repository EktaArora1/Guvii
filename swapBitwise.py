a,b=list(map(int,input().split()))
x=a^b
a=x^a
b=x^b
print(a,'',b)
