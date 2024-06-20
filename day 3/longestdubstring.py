s=input()
i=1
m=1
n=1
while i<len(s):
    if ord(s[i-1])+1==ord(s[i]):
        n+=1
    else:
         m=max(m,n)
         n=1
    m=max(m,n)
    i+=1
print(m)

    
    
    
