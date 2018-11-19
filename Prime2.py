def isPrime(j):
    for i in range(2, j):
        if j % i ==0:
            return False
    return j
a=int(input())
b=int(input())
for j in range(a+1,b):
  c=isPrime(j)
  if(c):
    print(c)
