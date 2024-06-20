r=int(input())
c=int(input())
def func(i,j,s,r,c,l):
     if i<0 or j>=c or j<0 or i>=r:
        return s
     if i==r-1 and j==c-1:
        s+=1
        return s
     l.append((i,j))
     if (i+1,j) not in l:
        s=func(i+1,j,s,r,c,l)
     if (i,j+1) not in l:
          s=func(i,j+1,s,r,c,l)
     if (i-1,j) not in l:
        s=func(i-1,j,s,r,c,l)
     if (i,j-1) not in l:
        s=func(i,j-1,s,r,c,l)
     l.pop()
     return s
s=func(0,0,0,r,c,[])
print(s)
    
        
