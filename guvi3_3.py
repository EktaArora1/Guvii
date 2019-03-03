num=int(input())
s=list(map(int,input().split()))
d=[]
for i in range(num):
    if i==s[i]:
        d.append(i)
print(*sorted(d)) if len(d)>0 else print(-1)
