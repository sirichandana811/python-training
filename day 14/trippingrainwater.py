l=list(map(int,input().split()))
n=len(l)
ml=[0]*n
print(ml)
mr=[0]*n
ml[0]=l[0]
mr[n-1]=l[n-1]
for i in range(1,n):
    if ml[i-1]>l[i]:
        ml[i]=ml[i-1]
    else:
        ml[i]=l[i]
for i in range(n-2,-1,-1):
    if mr[i+1]>l[i]:
        mr[i]=mr[i+1]
    else:
        mr[i]=l[i]
s=0
for i in range(n):
    s+=min(ml[i],mr[i])-l[i]
print(s)
    
            
        
        
        
    
    
