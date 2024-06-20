n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
def isprime(n):
    if n==1 or n==0:
        return 0
    if n==2:
        return 1
    i=2
    while i*i<=n:
        if n%i==0:
            return 0
        i=i+1
    else:
        return 1
s=0
for i in range(1,n):
    n1=l[i]-1
    while n1>l[i-1]:
        if isprime(n1)==1:
            s+=n1
            break
        n1-=1
print(s)
        
        
