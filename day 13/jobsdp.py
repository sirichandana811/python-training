l=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
m=0
n=len(l)
l1=[a[i] for i in range(n)]
for i in range(1,n):
    for j in range(i):
        if l[i][0]>=l[j][1] and l1[i]<l1[j]+a[i]:
            l1[i]=l1[j]+a[i]
print(max(l1))
            
