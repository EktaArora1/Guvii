n=input()
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
v=['a','e','i','o','u','A','E','I','O','U']
if n in a:
  if n in v:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("Invalid")
