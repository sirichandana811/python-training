n1=int(input())
n2=int(input())
if n1>n2:
    n=n2
else:
    n=n1
for i in range(2,n//2+1):
    if n1%i==0 and n2%i==0:
        print("not co-prime")
        break
else:
    print("co-prime")
    
