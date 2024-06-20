l=list(map(int,input().split()))
s=int(input())
n=len(l)
d=[[0 for i in range(s+1)] for i in range(n+1)]
for i in range(n+1):
   d[i][0]=1
for i in range(1,n+1):
    for j in range(1,s+1):
        if l[i-1]>j or d[i-1][j]==1:
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=d[i-1][j-l[i-1]]
        
print(d)
if d[-1][-1]==1:
    print("yes")
else:
    print("no")
        
