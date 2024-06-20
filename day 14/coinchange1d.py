c=list(map(int,input().split()))
m=int(input())
l=[0]*(m+1)
for i in range(1,m+1):
    l[i]=-1
l[0]=0
for i in l:
    for j in range(1,m+1):
        if j>=i:
            if l[j-i]!=-1:
                if l[j]!=-1:
                    l[j]=min(l[j],l[j-i])
            else:
                l[j]=l[j-i]
print(l[-1])
