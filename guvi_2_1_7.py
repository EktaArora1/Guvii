arr=list(input())
for i in range(1,len(arr),2):
    print(arr[i]+arr[i-1],end='')
