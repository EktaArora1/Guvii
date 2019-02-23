n,k=map(int,input().split())
s=list(map(int,input().split()))
countsOfNum=False
for i in s:
    if i==k:
        countsOfNum=True
print('yes') if countsOfNum else print('no')
