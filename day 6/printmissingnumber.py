n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
n1=n*(n+1)//2
print(n1-sum(l))
