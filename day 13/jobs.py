l=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
m=0
n=len(l)
l1=[0 for i in range(n)]
print(l1)
for i in range(n):
    for j in range(i+1,n):
        if l[i][0]>l[j][0]:
            l[i],l[j]=l[j],l[i]
            a[i],a[j]=a[j],a[i]
print(l,a)
s=0
for i in range(n):
  if l1[i]!=1:
    s=a[i]
    l1[i]=1
    k=l[i][1]
    for j in range(i+1,n):
      if k<=l[j][0]:
         s+=a[j]
         k=l[j][1]
         l1[j]=1
    print(s)
  if m<s:
        m=s
print(m,l1)
    
    
    
    
    
