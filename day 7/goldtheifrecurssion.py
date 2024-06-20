n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
def func(l):
      if len(l)==1:
        return l[0]
      if len(l)==0:
          return 0
      if len(l)==2:
          return max(l)
      n1=func(l[2:])
      n2=func(l[3:])
      return max(n1+l[0],n2+l[1])
print(func(l))
    



    
    
