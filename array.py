n,k=map(int,input().split())
arr=[]
for i in range(n):
  j=int(input())
  arr.append(j)
s=0
if(n>=k):
  for l in range(k):
    s=s+arr[l]
print(s)
