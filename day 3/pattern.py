n=int(input())

for i in range(n):
    n1=97
    for j in range(n-i):
        print("_",end=" ")
    for k in range(i+1):
        print(chr(n1),end=" ")
        n1=n1+1
    n1-=1
    for j1 in range(i):
        n1=n1-1
        print(chr(n1),end=" ")
        
    for j in range(n-i):
        print("_",end=" ")
    print("")
    
        
