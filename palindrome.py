def isPal(str):
  i = 0
  j = len(str) - 1
  while(i <= j):
    if(str[i] != str[j]):
      return False
    i += 1
    j -= 1
  return True
  
n=int(input())
if(isPal(str(n))):
  print"Yes"
else:
  print"No"
