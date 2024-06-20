class node:
    def __init__(self):
        self.d={}
        self.flag=0
        self.dict={}
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,s):
        t=self.root
        for i in s:
            if i not in t.d:
                t.d[i]=node()
                t.dict[i]=1
            elif i in t.d:
                t.dict[i]+=1
            t=t.d[i]
        t.flag=1
    def search(self,s):
     t=self.root
     for i in s:
         if i in t.d:
             t=t.d[i]
         else:
            return 0
     if t.flag==1:
         return 1
     else:
         return 0
    def prefix(self,s):
        t=self.root
        m=0
        for i in s:
            if i in t.d:
                m=t.dict[i]
                t=t.d[i]
            else:
                return 0
        return m
    
    def fun(self,t,s,l):
        if t.flag==1:
            l.append(s)
        for i in t.d:
           l=self.fun(t.d[i],s+i,l)
        return l
    def prefixwords(self,s):
        t=self.root
        for i in s:
            if i in t.d:
                t=t.d[i]
            else:
                return 0
        l=self.fun(t,s,[])
        print(l)
    def fun1(self,t,s,m,l):
        if t.flag==1:
            if m<len(s):
               l=[]
               m=len(s)
               l.append(s)
            elif m==len(s):
                l.append(s)
        for i in t.d:
           m,l=self.fun1(t.d[i],s+i,m,l)
        return m,l
    def longestprefix(self,s):
       t=self.root
       for i in s:
           if i in t.d:
               t=t.d[i]
           else:
               return 0
       m,l=self.fun1(t,s,0,[])
       return l
t1=tries()
t1.insert("word")
t1.insert("wo")
t1.insert("wold")
t1.insert("appl")
t1.insert("apri")
t1.insert("word")
print(t1.search("apple"))
print(t1.prefix("word"))
t1.prefixwords("wo")
l=list(map(str,input().split()))
m1=0
s=""
l1=[]
for i in l:
    m=t1.longestprefix(i)
    l1=m+l1
l1.sort()
print(l1)
print(l1[0])
