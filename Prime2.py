a=int(input)
b=int(input)
for j in range(a,b):
  for i in range(b):
    if(j%i==0):
      break
    else:
      print(j)
