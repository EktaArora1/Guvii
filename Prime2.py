def isPrime(j):
    for i in range(2, int(n**0.5) + 1):
        if j % i ==0:
            return False
    return i
a=int(input())
b=int(input())
for j in range(a,b):
  c=isPrime(j)
  if(c):
    print(c)
