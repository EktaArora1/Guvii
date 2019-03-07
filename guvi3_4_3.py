s=input()
i=0
c=0
m=0
fl=0
while i<len(s):
  if s[i]=='a' and fl==0:
    c+=1
    fl=1
    i+=1
  elif s[i]=='b' and fl==1:
    c+=1
    fl=0
    i+=1
  else:
    if c>m:
      m=c
      c=0
    if s[i]!='a':
      i+=1
    c=0
    fl=0
if c>m:
  print(c)
else:
  if m==1:
    print(0)
  else:
    print(m)
