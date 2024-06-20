l=list(map(int,input().split()))
m=l[0]
s=1
for i in range(1,len(l)):
    if m<l[i]:
        m=l[i]
        s+=1
s1=1
m2=l[len(l)-1]
for i in range(len(l)-2,-1,-1):
    if m2<l[i]:
        m2=l[i]
        s1+=1
print(s,s1)
