n=input()
c=0
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d=['0','1','2','3','4','5','6','7','8','9']
for i in n:
    if i not in a and i not in d and i!=" ":
        c+=1
print(c)
