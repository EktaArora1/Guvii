n=input()
m=input()
if(len(n)!=len(m)):
    print("no")
else:
    m1=['0']*256
    n1=['0']*256
    
    for i in range(len(n)):
        if (m1[ord(m[i])] != n1[ord(n[i])]):
            print("no")
        m1[ord(m[i])] = i + 1
        n1[ord(n[i])] = i + 1
    print("yes")
