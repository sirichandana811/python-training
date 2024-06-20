n=int(input())
l=[]
for i in range(n):
    l1=[]
    for j in range(n):
        l1.append(' ')
    l.append(l1)
l2=[]
c1=0
r2=int(input())
c2=int(input())
def func(i,j,r,c,d1,d2,c1,m):
  if i==n:
        l2.append(l.copy())
        print(l2)
        if m<c1:
            m=c1
        #print(l2)
        return m
  if i==r2:
     m=func(i+1,j,r,c,d1,d2,c1,m)
     return m
  for j in range(n):
   if m<c1:
       m=c1 
   if j!=c2 and i not in r and j not in c and j-i not in d1 and i+j not in d2:   
    l[i][j]='q'
    r.append(i)
    c.append(j)
    d1.append(j-i)
    d2.append(i+j)
    c1+=1
    m=func(i+1,j,r,c,d1,d2,c1,m)
    l[i][j]=' '
    r.pop()
    c.pop()
    d1.pop()
    d2.pop()
    c1-=1
  return m
c1=func(0,0,[],[],[],[],0,0)
print(c1)

