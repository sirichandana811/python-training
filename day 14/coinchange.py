c=list(map(int,input().split()))
m=int(input())
l=[[0 for i in range(m+1)]]*(len(c)+1)
for i in range(1,m+1):
    l[0][i]=9999
for i in range(1,len(c)+1):
    for j in range(1,m+1):
        if c[i-1]>j:
            l[i][j]=l[i-1][j]
        else:
            l[i][j]=min(l[i-1][j],l[i][j-c[i-1]]+1)
if l[-1][-1]==9999:
    print(-1)
else:
    print(l[-1][-1])
