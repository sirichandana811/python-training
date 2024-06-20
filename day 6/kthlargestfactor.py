n=int(input())
k=int(input())
i=n
while k!=0:
    if n%i==0:
        k-=1
    if k==0:
        break
    i-=1
print(i)
    
