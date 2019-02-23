n,k=map(int,input().split())
s=list(map(int,input().split()))
countsOfNum=0
for i in s:
    if i==k:
        countsOfNum+=1
print(countsOfNum)
