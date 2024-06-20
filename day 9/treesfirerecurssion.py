'''n=int(input())
l=[]
for i in range(n):
    l1=[]
    for j in range(n):
        l1.append(int(input()))
    l.append(l1)
print(l)'''
l=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
r=int(input())
c=int(input())
def func(r,c,l,n):
  if l[r][c]==1:
    l[r][c]=0
    if r>0:
        func(r-1,c,l,n)
    if r<n-1:
        func(r+1,c,l,n)
    if c>0 :
        func(r,c-1,l,n)
    if c<n-1:
        func(r,c+1,l,n)
    
  
func(r,c,l,6)
c=0
print(l)
for i in range(6):
    for j in range(6):
        if l[i][j]==1:
            c+=1
print(c)       
