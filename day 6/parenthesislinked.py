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
    def balanced(self):
        l=[]
        t=self.head
        n=0
        while t:
            n+=1
            if t.data=="(" or t.data=="[" or t.data=="{":
                l.append(t.data)
            else:
                if not l:
                    return n
                elif t.data==")" and l.pop()!="(":
                    return n
                elif t.data=="]" and l.pop()!="[":
                    return n
                elif t.data=="}" and l.pop()!="{":
                    return n
            
            t=t.nxt
        if l==[]:
                 return -1
        else:
                return n
        
            
l1=dll()
l1.addback("(")
l1.addback("[")
l1.addback("]")
l1.addback("{")
l1.addback("}")
l1.addback(")")
l1.display()
print(l1.balanced())
