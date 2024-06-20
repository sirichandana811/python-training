l=list(map(int,input().split()))
s=int(input())
def func(l1,i,m):
    if sum(l1)==s:
        return 1
    for j in range(i,len(l)):
        m=func(l1+[l[j]],j+1,m)
    return m
print(func([],0,0))
