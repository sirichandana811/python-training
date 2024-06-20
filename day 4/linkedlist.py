class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while t!=None:
            print(t.data)
            t=t.nxt
    def addback(self,x):
        t=self.head
        while t.nxt!=None:
            t=t.nxt
        t.nxt=node(x)
    def addfront(self,x):
        t=node(x)
        t.nxt=self.head
        self.head=t
    def addeven(self):
        t=self.head
        s=0
        while t!=None:
            if t.data%2==0:
                s+=t.data
            t=t.nxt
        print(s)
    def search(self,x):
        t=self.head
        f=1
        while t!=None:
            if t.data==x:
                return "found"
                
            t=t.nxt
        return "not found"
    def middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.nxt!=None:
            slow=slow.nxt
            fast=fast.nxt.nxt
        print("middle=",slow.data)
    def printpos(self):
        t1=self.head
        t2=self.head
        while t1:
            t2=t1.nxt
            while t2:
                print(t1.data,t2.data)
                t2=t2.nxt
            t1=t1.nxt
    def leneo(self):
        f=self.head
        while f and f.nxt:
            f=f.nxt.nxt
        if f:
            print("odd")
        else:
            print("even")
    def largestsubarray(self):
        s=1
        t=self.head
        m=1
        while t.nxt:
            if (t.data+1)==t.nxt.data:
                s+=1   
            else:
                m=max(s,m)
                s=1
            t=t.nxt
        m=max(m,s)
        print(m)
    def bubblesort(self):
        t1=self.head
        t3=None
        c=0
        f=1
        while t1:
            t2=self.head
            while t2.nxt!=t3:
                if t2.data>t2.nxt.data:
                    f=0
                    temp=t2.data
                    t2.data=t2.nxt.data
                    t2.nxt.data=temp
                t2=t2.nxt
            if f==0:
                break
            t3=t2
            t1=t1.nxt
        print("sorted",c)
    def reverse(self):
        
l1=sll()
l1.head=node(19)
l1.addback(20)
l1.addback(21)
l1.addback(23)
l1.addback(24)
l1.addback(18)
l1.display()
l1.bubblesort()
l1.display()
#l1.middle()
#l1.printpos()
#l1.leneo()
#l1.largestsubarray()
