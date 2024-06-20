n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
'''d={}
for i in l:
    if i in d:
             d[i]+=1
             if d[i]>n//2:
                    print(i)
                    break
    else:
        d[i]=1'''
c=1
p=l[0]
for i in range(1,n):
    if(l[i]==p):
        c=c+1
    else:
        c=c-1
        if c==0:
            c=1
            p=l[i]
print(p)
    
    
             
