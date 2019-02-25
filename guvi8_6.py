c=False
n=int(input())
for i in range(2,int(n**0.5)+2):
    if n%i==0:
        c=True
print('yes') if c else print('no')
