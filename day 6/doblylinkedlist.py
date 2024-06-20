class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.nxt=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            self.tail.nxt=node(x)
            self.tail.nxt.prev=self.tail
            self.tail=self.tail.nxt
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            self.head.prev=node(x)
            self.head.prev.nxt=self.head
            self.head=self.head.prev
    def display(self):
        t=self.head
        while t!=self.tail.nxt:
            print(t.data)
            t=t.nxt
    def linearsearch(self,x):
        t1=self.head
        t2=self.tail
        while t1!=t2.nxt and t1.prev!=t2.nxt:
            if t1.data==x or t2.data==x:
                print("found")
                break
            t1=t1.nxt
            t2=t2.prev
        else:
            print("notfound")
    def evenodd(self):
       t1=self.head
       t2=self.tail
       while t1!=t2.nxt and t1!=t2:
           t1=t1.nxt
           t2=t2.prev
       if t1==t2:
               print("odd")
       else:
               print("even")
    def palindrome(self):
        t1=self.head
        t2=self.tail
        while t1!=t2.nxt and t1!=t2:
            if t1.data!=t2.data:
                print("not palindrome")
                break
            t1=t1.nxt
            t2=t2.prev
        else:
            print("palindrome")
           
    def swapdata(self):
        t1=self.head
        t2=self.head
        while t2:
            t1=t1.nxt
            t2=t2.nxt.nxt
        t=self.head
        while t1:
            t.data,t1.data=t1.data,t.data
            t=t.nxt
            t1=t1.nxt
    def swapdata1(self):
        t1=self.head
        t2=self.tail
        while t1!=t2.nxt:
            t1=t1.nxt
            t2=t2.prev
        t=self.head
        while t1:
            t.data,t1.data=t1.data,t.data
            t=t.nxt
            t1=t1.nxt
    def swaplink(self):
       
       t1=self.head
       t2=self.tail
       while t1!=t2.nxt:
            t1=t1.nxt
            t2=t2.prev
       self.head.prev=self.tail
       self.tail.next=self.head
       t1.prev=None
       t2.nxt=None
       self.head=t1
       self.tail=t2
       print(self.tail.prev.prev.data)
    def swapadjlink(self):
       t1=self.head
       t2=t1.nxt
       self.head=self.head.nxt
       t3=None
       while t2.nxt:
           if t3:
               t3.nxt=t2
           t1.nxt=t2.nxt
           t2.nxt.prev=t1
           t2.nxt=t1
           t2.prev=t1.prev
           t1.prev=t2
           t1=t1.nxt
           t2=t1.nxt
           t3=t1.prev
    def oed(self,t,d):
        if not t:
            return d
        if t.data%2==0:
            d-=t.data
        else:
            d+=t.data
        return l1.oed(t.nxt,d)
    def prime(self,i,n):
       if n==1:
            return 1
       if n==4:
           return 0
       if i*i>n:
           return 1
       if n%i==0:
           return 0
       return l1.prime(i+1,n)
    def countp(self,t,c):
       if not t:
           return c
       if l1.prime(2,t.data)==1:
           c+=1
       return l1.countp(t.nxt,c)       
l1=dll()
l1.addback(1)
l1.addback(3)
l1.addback(4)
l1.addback(5)
l1.addback(6)
l1.addback(9)
l1.display()
#l1.linearsearch(0)
#l1.evenodd()
#l1.palindrome()
#l1.swapdata()
#l1.display()
#l1.swapdata1()
#l1.display()
#l1.swapadjlink()
#print("sum=",abs(l1.oed(l1.head,0)))
print("count=",l1.countp(l1.head,0))

        

        
