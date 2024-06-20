d={5:[7,3],7:[5,4,3],4:[7,8,2],3:[5,7,8],2:[4,8],8:[3,2,4]}
def func(i,l,d):
    l.append(i)
    for i in d[i]:
        if i not in l:
            func(i,l,d)
    return l
def findallpaths(i,l,d):
    l.append(i)
    
    print(l)
        
    for i in d[i]:
        if i not in l:
            findallpaths(i,l,d)
    l.pop()
def findcost(i,l,d1,s):
    l.append(i)
    if i==2:
        print(l)
        print(s)
        l.pop()
        return
    for i in d1[i]:
        j,k=i[0],i[1]
        if j not in l:
            findcost(j,l,d1,s+k)
    l.pop()
def weightForPath(i,l,j,s):
    l.append(i)
    if i==j: 
        print(l)
        print(s)
        l.pop()
        return
    for i in d[i]:
        k,r=i[0],i[1]
        if k not in l:
            weightForPath(k,l,j,s+r)
    l.pop()

def shortestPath(i,l,j,s,m,l1):
    l.append(i)
    if i==j:
        if s<m:
            m=s
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[i]:
        k,r=i[0],i[1]
        if k not in l:
            m,l1=shortestPath(k,l,j,s+r,m,l1)
    l.pop()
    return m,l1
def bfs(i,q,v):
    q.append(i)
    while q:
      for i in d[q[0]]:
        if i not in q and i not in v:
             q.append(i)
      v.append(q.pop(0))
    print(v)
def dijk(n,q,v):
    q.append(n)
    d1={}
    for i in d:
        d1[i]=float('inf')
    d1[n]=0
    m=5
    p=float('inf')
    while q:
      m=99999
      for i in q:
            if d1[i]<m:
                m=d1[i]
                n=i
      for i in d[n]:
        if i[0] not in v:
             q.append(i[0])
             if d1[i[0]]>i[1]+d1[n]:
                 d1[i[0]]=i[1]+d1[n]
                    
      v.append(n)
      q.remove(n)
    print(d1)
l=[]
i=list(d.keys())[0]
#print(func(i,[],d))
#findallpaths(i,l,d)
#d={5:[(7,1),(3,2)],7:[(5,1),(3,2),(4,3)],4:[(7,3),(8,2),(2,1)],8:[(3,2),(2,2),(4,2)],3:[(5,7,2),(8,2)],2:[(4,1),(8,2)]}
#weightForPath(i,l,j,0)
#d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
#d={9:[8,5],8:[9,4,3],4:[8,2,5],3:[8],2:[4],5:[9,4]}
#print(i)
d={5:[(7,1),(3,2)],7:[(5,1),(4,3),(3,2)],4:[(7,3),(8,2),(2,1)],8:[(3,2),(4,2),(2,2)],3:[(5,2),(7,2),(8,2)],2:[(4,1),(8,2)]}
#d={5:[(7,1),(3,2)],7:[(5,1),(4,2),(3,3)],4:[(7,3),(8,2),(2,1)],8:[(3,2),(4,2),(2,2)],3:[(5,2),(7,2),(8,2)],2:[(4,1),(8,2)]}
dijk(5,[],[])
'''for j in d.keys():
  print(shortestPath(i,l,j,0,99999,[]))
#print(m)
#print(l1)'''
