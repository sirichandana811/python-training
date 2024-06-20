l=list(map(int,input().split()))
n=len(l)
i=0
j=1
k=2
while k<n:
    if  l[i]>l[j]:
        l[i],l[j]=l[j],l[i]
    if l[j]>l[k] :
        l[j],l[k]=l[k],l[j]
    if l[i]>l[j]:
           l[i],l[j]=l[j],l[i]
    i+=1
    j+=1
    k+=1
print(l)
        
