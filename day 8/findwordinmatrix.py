n=int(input())
l=[]
for i in range(n):
    l1=[]
    for i in range(n):
        l1.append(input())
    l.append(l1)
s=input()
v=[[0]*n for i in range(n)]
print(l)
def func(r,c,l,n,s,i):
  if i==len(s):
      return 1
  if r<0 or c<0 or c>n-1 or r>n-1 or i>=len(s) or v[r][c]==1:
      return 0
  if l[r][c]==s[i] and v[r][c]==0:
       v[r][c]=1
       n1=func(r-1,c,l,n,s,i+1)
       n1=func(r+1,c,l,n,s,i+1)
       n1=func(r,c-1,l,n,s,i+1)
       n1=func(r,c+1,l,n,s,i+1)
       v[r][c]=0
       return n1
for i in range(n):
    for j in range(n):
         if func(i,j,l,n,s,0)==1:
             print("yes")
            
            
            

    
