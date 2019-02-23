allfactors=0
n=int(input())
for i in range(2,n):
    if n%i==0:
        allfactors+=1
print('no') if allfactors>0 else print('yes')
