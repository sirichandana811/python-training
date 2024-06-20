l=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
def func(i,j,r,c,n):
  if i<0 or j<0 or j>=r or i>=c:
        return n
  if l[i][j]==1:
    l[i][j]=0
    n+=1
    n=func(i-1,j,r,c,n)
    n=func(i,j-1,r,c,n)
    n=func(i+1,j,r,c,n)
    n=func(i,j+1,r,c,n)
    '''q=(n1+n2+n3+n4)
    print(q)'''
    return n
  return n
c=0
m=0
for i in range(len(l)):
    for j in range(len(l[0])):
        if l[i][j]==1:
            c+=1
            s=func(i,j,len(l),len(l[0]),0)
            #print(s)
            if m<s:
                m=s
            
print(m)
