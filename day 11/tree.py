class node:
  def __init__(self,n):
    self.data=n
    self.left=None
    self.right=None
class tree:
    def __init__(self):
        self.root=None
    def creat(self,root,x):
        if self.root==None:
            self.root=node(x)
        if root==None:
            return node(x)
        elif(root.data>x):
            root.left=self.creat(root.left,x)
        else:
            root.right=self.creat(root.right,x)
        return root
    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
    def sumn(self,root):
        if root==None:
            return 0
        if root:
          return root.data+self.sumn(root.left)+self.sumn(root.right)
    def sume(self,root):
        if root==None:
            return 0
        if root.data%2==0:
             return root.data+self.sume(root.left)+self.sume(root.right)
        return self.sume(root.left)+self.sume(root.right)
    def sumd(self,root):
          if root==None:
            return 0
          if root.data%2==0:
             return root.data+self.sumd(root.left)+self.sumd(root.right)
          return -root.data+self.sumd(root.left)+self.sumd(root.right)
    def height(self,root):
        if root==None:
            return -1
        n1=1+self.height(root.left)
        n2=1+self.height(root.right)
        return max(n1,n2)
    def balanced(self,root):
        if root==None:
            return -1
        return abs(self.balanced(root.left)-self.balanced(root.right))<=1
    #def balanced(self,)
    def countleaf(self,root):
        if root==None:
            return 0
        if root.right==None and root.left==None:
            return 1
        return self.countleaf(root.right)+self.countleaf(root.left)
    def countleafdata(self,root):
        if root==None:
            return 0
        if root.right==None and root.left==None:
            return root.data
        return self.countleafdata(root.right)+self.countleafdata(root.left)
    def depth(self,root,n,i):
        if root==None:
            return 0
        if root.data==n:
            return i
        if root.data>n:
            return self.depth(root.left,n,i+1)
        else:
            return self.depth(root.right,n,i+1)
    def search(self,root,n):
        if root==None:
            return False
        if root.data==n:
            return self.depth(t1.root,n,0)
        if root.data>n:
            return self.search(root.left,n)
        else:
            return self.search(root.right,n)
    d={}
    def topview(self,root,d,c,i):
      if root==None:
        return
      if c not in d : 
        d[c]=[root.data,i]
      else:
        if i<d[c][1]:
          d[c]=[root.data,i]
          
      self.topview(root.left,d,c-1,i+1)
      self.topview(root.right,d,c+1,i+1)
    def topview1(self,root):
        l=[]
        d={}
        l.append([root,0])
        while l:
          if l[0][1] not in d:
              d[l[0][1]]=l[0][0].data
          if l[0][0].left:
                 l.append([l[0][0].left,l[0][1]-1])
          if l[0][0].right:
                l.append([l[0][0].right,l[0][1]+1])
          l.pop(0)
        for i in sorted(d):
          print(d[i],end="->")
        
    def bottomview(self,root,d,c,i):
      if root==None:
        return
      if c not in d1 : 
        d1[c]=[root.data,i]
      else:
        if i>=d1[c][1]:
          d1[c]=[root.data,i] 
      self.bottomview(root.left,d1,c-1,i+1)
      self.bottomview(root.right,d1,c+1,i+1)
    def bottomview1(self,root):
        l=[]
        d={}
        l.append([root,0])
        while l:
          d[l[0][1]]=l[0][0].data
          if l[0][0].left:
                 l.append([l[0][0].left,l[0][1]-1])
          if l[0][0].right:
                l.append([l[0][0].right,l[0][1]+1])
          l.pop(0)
        for i in sorted(d):
          print(d[i],end="->")
    def leftview(self,root,l,c):
      if not root:
        return
      if l==[]:
        print(root.data)
        l.append(c)
      if c not in l:
        l.append(c)
        print(root.data)
      self.leftview(root.left,l,c+1)
      self.leftview(root.right,l,c+1)
    def rightview(self,root,l,c):
      if not root:
        return
      if l==[]:
        print(root.data)
        l.append(c)
      if c not in l:
        l.append(c)
        print(root.data)
      self.rightview(root.right,l,c+1)
      self.rightview(root.left,l,c+1)
t1=tree()
t1.creat(t1.root,4)
t1.creat(t1.root,2)
t1.creat(t1.root,7)
t1.creat(t1.root,1)
t1.creat(t1.root,3)
t1.creat(t1.root,6)
t1.creat(t1.root,9)
t1.creat(t1.root,5)
'''t1.preorder(t1.root)
t1.inorder(t1.root)
t1.postorder(t1.root)'''
'''print(t1.balanced(t1.root))
print(t1.sumn(t1.root))
print(t1.sume(t1.root))
print(abs(t1.sumd(t1.root)))
print(t1.height(t1.root))
print(t1.countleaf(t1.root))
print(t1.countleafdata(t1.root))
n=int(input())
print(t1.search(t1.root,n))
d={}
t1.topview(t1.root,d,0,0)
t1.topview1(t1.root)
print(d)'''
d1={}
t1.bottomview(t1.root,d1,0,0)
t1.bottomview1(t1.root)
print(d1)
'''
#t1.bottomview("bottom="+t1.root)
t1.leftview(t1.root,[],0)
t1.rightview(t1.root,[],0)'''



    
