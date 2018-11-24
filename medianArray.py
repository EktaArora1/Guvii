n=int(input())
arr=[]
arr=input().split(' ')
arr=sorted(arr)
arr = list(map(int, arr))
print(arr[n//2])
