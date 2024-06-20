class node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def insert(self,root,x):
        if self.root is None:
            self.root=node(x)
            return self.root
        if root==None:
            return node(x)
        elif root.data>x:
            root.left=self.insert(root.left,x)
        else:
           root.right=self.insert(root.right,x)
        return root
           
           
    def inorder(self,root):
        if root :
            self.inorder(root.left)
            print(root.data,end="->")
            self.inorder(root.right)
    
    def sum(self,root):
        
        if root is None:
            return 0
        else:
            return root.data + self.sum(root.left) + self.sum(root.right)
    def diff(self,root):
        if root is None:
            return 0
        if root.data%2==0:
            return root.data + self.diff(root.left) + self.diff(root.right)

        return -root.data+self.diff(root.left) + self.diff(root.right)
    def even(self,root):
        if root is None:
            return 0
        if root.data%2==0:
            return root.data + self.even(root.left) + self.even(root.right)
        else:
            return self.even(root.left) + self.even(root.right)

    def odd(self,root):
        if root is None:
            return 0
        if root.data%2!=0:
            return root.data + self.odd(root.left) + self.odd(root.right)
        else:
            return self.odd(root.left) + self.odd(root.right)
            
        


        
t1=tree()
t1.insert(t1.root,10)
t1.insert(t1.root,5)
t1.insert(t1.root,1)
t1.insert(t1.root,7)
t1.insert(t1.root,6)
t1.insert(t1.root,8)
t1.insert(t1.root,20)
t1.insert(t1.root,25)
t1.inorder(t1.root)
print()
print(t1.even(t1.root))
print()
print(t1.odd(t1.root))
print()

print(t1.diff(t1.root))


