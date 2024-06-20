s=input()
n=len(s)
def func(i,j,s):
    while i>=0 and j<n:
        if s[i]==s[j]:
           i-=1
           j+=1
        else:
            break
    i+=1
    j-=1
    return (j-i+1)
m=0
for i in range(n):
    if n%2==0 and i<n-1:
        j=i+1
        print(i,j)
        m1=func(i,j,s)
        print(m1)
        if m<m1:
            m=m1
    else:
        m2=func(i,i,s)
        if m<m2:
            m=m2
print(m)
